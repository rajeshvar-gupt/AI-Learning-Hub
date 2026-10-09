# PY-010 · HTTP and JSON fundamentals

Prerequisites: [functions](../01-fundamentals/04-functions-and-score-summary.md) and [collections](../01-fundamentals/06-collections-in-depth.md). Goal: distinguish response status, serialization and application validation.

## Request and response

A request contains a method, URL, headers and sometimes a body. GET commonly retrieves a representation; POST commonly submits data. Actual behavior depends on the API. A response has a status, headers and optional body. HTTPS encrypts transport; it does not guarantee correct data.

| Part | Illustrative value | Meaning |
|---|---|---|
| Method/path | GET /courses/python | Operation and resource |
| Request header | Accept: application/json | Desired representation |
| Status | 200 | Successful response |
| Response header | Content-Type: application/json | Declared format |
| Body | {"title":"Python","lessons":10} | Serialized data |

This endpoint is illustrative, not a live service.

## JSON is text

```python
import json
course = json.loads('{"title":"Python","active":true,"note":null}')
print(course["title"])
print(course["active"])
print(course["note"])
print(json.dumps({"lessons": 10}))
```

Output: Python, True, None and {"lessons": 10} on separate lines. Objects become dictionaries, arrays become lists, and true/false/null become True/False/None. JSON strings require double quotes. loads parses text; dumps produces text. Parsing success does not prove required fields are valid.

## Status before data

| Status | Typical meaning |
|---|---|
| 200 | Success |
| 204 | Success without response content |
| 401 / 403 | Authentication required/failed, or forbidden access |
| 404 | Not found |
| 429 | Too many requests |
| 500 | Server error |

Error bodies can be JSON, HTML or empty. A live client also needs timeouts and handling for connection failures. Retrying every error can repeat side effects; follow the API's contract.

## Offline response lab

```bash
python3 subjects/python/examples/http_json_demo.py
```

Run from repository root; use py on Windows if appropriate. [Code](../examples/http_json_demo.py) uses simulated responses and makes no network requests.

Design order: require 200 for this specific representation; check the media type; parse JSON; require an object; validate title and lesson count. Return only the needed fields. Checking exact int rejects JSON true as a count.

Expected output:

```text
Course: Python basics (10 lessons)
Error: HTTP 404: course response unavailable.
Error: Lesson count must be a nonnegative integer.
```

The helper expects an integer status and text header/body. It accepts application/json, not every JSON-based media type. It does not authenticate, retry, cap network response sizes or implement network I/O. Status 204 is valid HTTP but not a usable course representation for this function.

```bash
python3 -m unittest discover -s subjects/python/examples -p 'test_http_json_demo.py' -v
```

[Questions](../../../assignments/PY-010/questions.md) · [Solutions](../../../assignments/PY-010/solutions.md). Next planned task: Python foundations review and integrated practice.

References, checked 9 October 2026: [Python Software Foundation — json](https://docs.python.org/3/library/json.html); [MDN — HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status).

Validation: all six response tests, the JSON snippet and the demo output passed on Python 3.12.14. No real HTTP request was made.
