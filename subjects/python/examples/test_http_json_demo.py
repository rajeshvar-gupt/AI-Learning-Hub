import unittest
from http_json_demo import parse_course_response

class ResponseTests(unittest.TestCase):
    def test_success(self):
        self.assertEqual(parse_course_response(200, "Application/JSON; charset=utf-8",
            '{"title":" Python ","lessons":0,"extra":123}'), {"title":"Python","lessons":0})

    def test_status_before_body(self):
        for status in [204,401,403,404,429,500]:
            with self.subTest(status=status):
                with self.assertRaisesRegex(ValueError, f"HTTP {status}"):
                    parse_course_response(status,"text/html","bad")

    def test_content_type(self):
        with self.assertRaisesRegex(ValueError,"application/json"):
            parse_course_response(200,"text/html","<html></html>")

    def test_json(self):
        for body in ["", "{", "{'title':'P'}"]:
            with self.subTest(body=body):
                with self.assertRaisesRegex(ValueError,"valid JSON"):
                    parse_course_response(200,"application/json",body)

    def test_shape(self):
        for body in ["[]","null","42",'"text"']:
            with self.subTest(body=body):
                with self.assertRaisesRegex(ValueError,"JSON object"):
                    parse_course_response(200,"application/json",body)

    def test_fields(self):
        for body in ['{}','{"title":" ","lessons":1}','{"title":4,"lessons":1}',
                     '{"title":"P"}','{"title":"P","lessons":-1}',
                     '{"title":"P","lessons":true}','{"title":"P","lessons":2.5}',
                     '{"title":"P","lessons":"2"}']:
            with self.subTest(body=body):
                with self.assertRaises(ValueError):
                    parse_course_response(200,"application/json",body)

if __name__ == "__main__":
    unittest.main()
