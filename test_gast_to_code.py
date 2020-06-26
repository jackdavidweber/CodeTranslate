import unittest2
import gast_to_code as gtc

gast_str = { "type": "str", "value": "hello world" }

gast_num = { "type": "num", "value": 47.47 }

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

    # test other types
    def test_nested_arr(self):
        self.assertEqual('["hello", [1, 2]]', gtc.gast_router(gast_arr, "py"))
        self.assertEqual('["hello", [1, 2]]', gtc.gast_router(gast_arr, "js"))


    # test logStatement
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


if __name__ == '__main__':
    unittest2.main()