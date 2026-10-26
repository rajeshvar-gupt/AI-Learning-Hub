"""SQLite idempotent dry-run scheduling; never sends a message."""
import hashlib
import json
import sqlite3
from datetime import datetime,timezone


def utc(value):
    dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    if dt.tzinfo is None:raise ValueError('timezone required')
    return dt.astimezone(timezone.utc).isoformat()


class Queue:
    def __init__(self,path=':memory:'):
        self.db=sqlite3.connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, due TEXT, payload TEXT, status TEXT)')

    def add(self,key,due,payload):
        if not isinstance(key,str) or not key or len(key)>100:raise ValueError('bounded nonempty idempotency key required')
        if not isinstance(payload,dict):raise ValueError('object payload required')
        encoded=json.dumps(payload,sort_keys=True,allow_nan=False)
        if len(encoded)>4000:raise ValueError('payload too large')
        due=utc(due)
        with self.db:
            row=self.db.execute('SELECT due,payload FROM jobs WHERE id=?',(key,)).fetchone()
            if row:
                if row!=(due,encoded):raise ValueError('same key reused with different content')
                return False
            self.db.execute('INSERT INTO jobs VALUES (?,?,?,?)',(key,due,encoded,'pending'))
        return True

    def dry_run(self,now):
        now=utc(now)
        with self.db:
            rows=self.db.execute("SELECT id,payload FROM jobs WHERE due<=? AND status='pending' ORDER BY due,id",(now,)).fetchall()
            self.db.executemany("UPDATE jobs SET status='simulated' WHERE id=?",[(r[0],) for r in rows])
        return [{'id':key,'payload_sha256':hashlib.sha256(payload.encode()).hexdigest(),'sent':False} for key,payload in rows]

    def close(self):self.db.close()
