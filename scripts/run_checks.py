"""One local entry point for behavioral suites and repository-link validation."""
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
for folder in ['tests','projects/beginner/student-score-summary','subjects/python/examples']:
    subprocess.run([sys.executable,'-m','unittest','discover','-s',folder,'-p','test_*.py','-v'],cwd=root,check=True)
subprocess.run([sys.executable,'scripts/check_release.py'],cwd=root,check=True)
