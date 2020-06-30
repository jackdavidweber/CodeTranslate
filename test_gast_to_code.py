import unittest2
import gast_to_code as gtc

gast_str = { "type": "str", "value": "hello world" }

gast_num = { "type": "num", "value": 47.47 }

gast_true = {"type": "bool", "value": 1}

gast_false = {"type": "bool", "value": 0}

gast_arr = {
	"type": "arr",
	"elts": 
		[
            {
                "type": "str",
                "value": "hello"
            },
            {
                "type": "arr",
                "elts":
                    [
                        {
                            "type": "num",
                            "value": 1
                        },
                        {
                            "type": "num",
                            "value": 2
                        }
                    ]
            }
		]
}

gast_logStatement_bool = {
            "type": "root",
            "body": [
                {
                    "type": "logStatement",
                    "args": [
                        {
                            "type": "bool",
                            "value": 0
                        }
                    ]
                }
            ]
        }

gast_logStatement = {
            "type": "root",
            "body": [
                {
                    "type": "logStatement",
                    "args": [
                        {
                            "type": "str",
                            "value": "hello world"
                        },
                        {
                            "type": "num",
                            "value": 5
                        }
                    ]
                }
            ]
        }

gast_varAssign_let = {
	"type": "root",
	"body": [
		{
			"type": "varAssign",
			"kind": "let",
			"varId": "x",
            "varValue": 
                {
                    "type": "num",
                    "value": 5
                }
        },
		]
}

gast_varAssign_const = {
	"type": "root",
	"body": [
		{
			"type": "varAssign",
			"kind": "const",
			"varId": "x",
            "varValue": 
                {
                    "type": "num",
                    "value": 5
                }
        },
		]
}

gast_multi_body = {
    "type": "root",
    "body": [
        { "type": "varAssign", "kind": "const", "varId": "x", "varValue": { "type": "num", "value": 5 } },
        { "type": "varAssign", "kind": "const", "varId": "x", "varValue": { "type": "num", "value": 5 } },
    ]
}

class TestGastToCode(unittest2.TestCase):
    # test primitives
    def test_primitive_str(self):
        self.assertEqual('"hello world"', gtc.gast_router(gast_str, "py"))
        self.assertEqual('"hello world"', gtc.gast_router(gast_str, "js"))

    def test_primitive_num(self):
        self.assertEqual('47.47', gtc.gast_router(gast_num,"py"))
        self.assertEqual('47.47', gtc.gast_router(gast_num,"js"))

    def test_primitive_true_js (self):
        self.assertEqual('true', gtc.gast_router(gast_true, "js"))

    def test_primitive_false_js (self):
        self.assertEqual('false', gtc.gast_router(gast_false, "js"))

    def test_primitive_true_py (self):
        self.assertEqual('True', gtc.gast_router(gast_true, "py"))

    def test_primitive_false_py (self):
        self.assertEqual('False', gtc.gast_router(gast_false, "py"))


    # test other types
    def test_nested_arr(self):
        self.assertEqual('["hello", [1, 2]]', gtc.gast_router(gast_arr, "py"))
        self.assertEqual('["hello", [1, 2]]', gtc.gast_router(gast_arr, "js"))


    # test logStatement
    def test_js_logStatement_bool (self):
        self.assertEqual('console.log(false)', gtc.gast_router(gast_logStatement_bool, "js"))

    def test_js_logStatement_two_arguments(self):
        self.assertEqual('console.log("hello world", 5)', gtc.gast_router(gast_logStatement, "js"))

    def test_py_logStatement_two_arguments(self):
        self.assertEqual('print("hello world", 5)', gtc.gast_router(gast_logStatement, "py"))

    # test varAssign
    def test_js_varAssign_let(self):
        self.assertEqual('let x = 5', gtc.gast_router(gast_varAssign_let, "js"))
   
    def test_py_varAssign_let (self):
        self.assertEqual('x = 5', gtc.gast_router(gast_varAssign_let, "py"))

    def test_js_varAssign_const(self):
        self.assertEqual('const x = 5', gtc.gast_router(gast_varAssign_const, "js"))
   
    def test_py_varAssign_const (self):
        self.assertEqual('x = 5', gtc.gast_router(gast_varAssign_const, "py"))

    # test multiple items in body
    def test_multi_body (self):
        self.assertEqual('x = 5\nx = 5', gtc.gast_router(gast_multi_body, "py"))

    # TODO: add elif and else if tests once new way of doing logstatements are merged
    def test_if (self):
        input_gast = {
            'type': 'root',
            'body': [{
                'type': 'if',
                 'body': [{
                     'type': 'logStatement',
                     'args': [{'type': 'str', 'value': 'This is true'}]
                    }],
                'orelse': [],
                'test': {'type': 'bool', 'value': 1}
                }]
            }
        expected_js = 'if (true) {\n\tconsole.log("This is true")\n}'
        # self.assertEqual(expected_js, gtc.gast_router(input_gast, "js"))

        expected_py = 'if (True):\n\tprint("This is true")'
        self.assertEqual(expected_py, gtc.gast_router(input_gast, "py"))


if __name__ == '__main__':
    unittest2.main()