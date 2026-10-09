"""Simulated HTTP responses only; no network requests."""
import json

def parse_course_response(status, content_type, body):
    if status != 200:
        raise ValueError(f"HTTP {status}: course response unavailable.")
    if content_type.split(";", 1)[0].strip().lower() != "application/json":
        raise ValueError("Expected application/json.")
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        raise ValueError("Response is not valid JSON.") from None
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object.")
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        raise ValueError("Course title must be nonempty text.")
    if type(data.get("lessons")) is not int or data["lessons"] < 0:
        raise ValueError("Lesson count must be a nonnegative integer.")
    return {"title": data["title"].strip(), "lessons": data["lessons"]}

def main():
    responses = [
        (200, "application/json; charset=utf-8", '{"title":"Python basics","lessons":10}'),
        (404, "application/json", '{"error":"Not found"}'),
        (200, "application/json", '{"title":"Python","lessons":true}'),
    ]
    for status, content_type, body in responses:
        try:
            course = parse_course_response(status, content_type, body)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"Course: {course['title']} ({course['lessons']} lessons)")

if __name__ == "__main__":
    main()
