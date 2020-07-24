import unittest2
import python.code_to_gast.py_main as py_main
import javascript.code_to_gast.js_main as js_main
import java.code_to_gast.java_main as java_main
from test.error_handler_helper import get_error_handler


class test_code_to_gast_loops(unittest2.TestCase):
    maxDiff = None

    def test_forRange(self):
        js_input = 'for (let i = 0; i < 10; i += 2) {\n\t5\n}'
        py_input = 'for i in range (0, 10, 2):\n\t5'
        java_input = 'for (int i = 0; i < 10; i += 2) {\n\t5;\n}'

        expected_gast = {
            'type':
                'root',
            'body': [{
                "type": "forRangeStatement",
                "init": {
                    "type": "varAssign",
                    "kind": "let",
                    "varId": {
                        "type": "name",
                        "value": "i"
                    },
                    "varValue": {
                        "type": "num",
                        "value": 0
                    }
                },
                "test": {
                    "type": "binOp",
                    "left": {
                        "type": "name",
                        "value": "i"
                    },
                    "op": "<",
                    "right": {
                        "type": "num",
                        "value": 10
                    }
                },
                "update": {
                    "type": "augAssign",
                    "left": {
                        "type": "name",
                        "value": "i"
                    },
                    "op": "+=",
                    "right": {
                        "type": "num",
                        "value": 2
                    }
                },
                "body": [{
                    "type": "num",
                    "value": 5
                }]
            }]
        }

        self.assertEqual(
            expected_gast,
            py_main.py_to_gast(py_input, error_handler=get_error_handler('py')))
        self.assertEqual(
            expected_gast,
            js_main.js_to_gast(js_input, error_handler=get_error_handler('js')))
        self.assertEqual(
            expected_gast,
            java_main.java_to_gast(java_input, error_handler="java"))

    def test_forRange_negative(self):
        js_input = 'for (let i = -25; i > -50; i -= 5) {\n\t5\n}'
        py_input = 'for i in range (-25, -50, -5):\n\t5'
        java_input = 'for (int i = -25; i > -50; i -= 5) {\n\t5;\n}'

        expected_gast = {
            'type':
                'root',
            'body': [{
                "type": "forRangeStatement",
                "init": {
                    "type": "varAssign",
                    "kind": "let",
                    "varId": {
                        "type": "name",
                        "value": "i"
                    },
                    "varValue": {
                        "type": "num",
                        "value": -25
                    }
                },
                "test": {
                    "type": "binOp",
                    "left": {
                        "type": "name",
                        "value": "i"
                    },
                    "op": ">",
                    "right": {
                        "type": "num",
                        "value": -50
                    }
                },
                "update": {
                    "type": "augAssign",
                    "left": {
                        "type": "name",
                        "value": "i"
                    },
                    "op": "-=",
                    "right": {
                        "type": "num",
                        "value": 5
                    }
                },
                "body": [{
                    "type": "num",
                    "value": 5
                }]
            }]
        }

        self.assertEqual(
            expected_gast,
            py_main.py_to_gast(py_input, error_handler=get_error_handler('py')))
        self.assertEqual(
            expected_gast,
            js_main.js_to_gast(js_input, error_handler=get_error_handler('js')))
        self.assertEqual(
            expected_gast,
            java_main.java_to_gast(java_input, error_handler="java"))

    def test_forOf(self):
        js_input = 'for (elem of [1, 2]) {\n\t5\n}'
        py_input = 'for elem in [1, 2]:\n\t5'

        expected_gast = {
            'type':
                'root',
            'body': [{
                "type": "forOfStatement",
                "init": {
                    "type": "name",
                    "value": "elem"
                },
                "iter": {
                    "type":
                        "arr",
                    "elements": [{
                        "type": "num",
                        "value": 1
                    }, {
                        "type": "num",
                        "value": 2
                    }]
                },
                "body": [{
                    "type": "num",
                    "value": 5
                }]
            }]
        }

        self.assertEqual(
            expected_gast,
            py_main.py_to_gast(py_input, error_handler=get_error_handler('py')))
        self.assertEqual(
            expected_gast,
            js_main.js_to_gast(js_input, error_handler=get_error_handler('js')))

    def test_forOf_with_java(self):
        js_input = 'for (elem of arr) {\n\t5\n}'
        py_input = 'for elem in arr:\n\t5'
        java_input = 'for (int elem : arr) {\n\t5;}'

        expected_gast = {
            'type':
                'root',
            'body': [{
                "type": "forOfStatement",
                "init": {
                    "type": "name",
                    "value": "elem"
                },
                "iter": {
                    "type": "name",
                    "value": "arr"
                },
                "body": [{
                    "type": "num",
                    "value": 5
                }]
            }]
        }

        self.assertEqual(
            expected_gast,
            py_main.py_to_gast(py_input, error_handler=get_error_handler('py')))
        self.assertEqual(
            expected_gast,
            js_main.js_to_gast(js_input, error_handler=get_error_handler('js')))
        self.assertEqual(
            expected_gast,
            java_main.java_to_gast(java_input, error_handler="java"))


if __name__ == '__main__':
    unittest2.main()
