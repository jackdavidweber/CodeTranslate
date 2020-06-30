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

gast_binOp_add = {'type': 'binOp', 'op': '+', 'left': {'type': 'num', 'value': 3}, 'right': {'type': 'num', 'value': 4}}

gast_binOp_bitwise = {'type': 'binOp', 'op': '&', 'left': {'type': 'num', 'value': 1}, 'right': {'type': 'num', 'value': 3}}

gast_binOp_add_sub_mult_div = {'type': 'binOp', 'op': '-', 'left': {'type': 'binOp', 'op': '+', 'left': {'type': 'num', 'value': 1}, 'right': {'type': 'num', 'value': 2}}, 'right': {'type': 'binOp', 'op': '/', 'left': {'type': 'binOp', 'op': '*', 'left': {'type': 'num', 'value': 3}, 'right': {'type': 'num', 'value': 4}}, 'right': {'type': 'num', 'value': 5}}}

gast_boolOp_and = {'type': 'boolOp', 'op': '&&', 'left': {'type': 'bool', 'value': 1}, 'right': {'type': 'bool', 'value': 0}}

gast_boolOp_or_and = {'type': 'boolOp', 'op': '||', 'left': {'type': 'bool', 'value': 1}, 'right': {'type': 'boolOp', 'op': '&&', 'left': {'type': 'bool', 'value': 0}, 'right': {'type': 'num', 'value': 4}}}

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

    def test_binOp_add (self):
        self.assertEqual('3 + 4', gtc.gast_router(gast_binOp_add, "py"))
        self.assertEqual('3 + 4', gtc.gast_router(gast_binOp_add, "js"))

    def test_binOp_bitwise (self):
        self.assertEqual('1 & 3', gtc.gast_router(gast_binOp_bitwise, "py"))
        self.assertEqual('1 & 3', gtc.gast_router(gast_binOp_bitwise, "js"))

    def test_binOp_add_sub_mult_div (self):
        self.assertEqual('1 + 2 - 3 * 4 / 5', gtc.gast_router(gast_binOp_add_sub_mult_div, "py"))
        self.assertEqual('1 + 2 - 3 * 4 / 5', gtc.gast_router(gast_binOp_add_sub_mult_div, "js"))

    def test_boolOp_and_py (self):
        self.assertEqual('True and False', gtc.gast_router(gast_boolOp_and, "py"))

    def test_boolOp_and_js (self):
        self.assertEqual('true && false', gtc.gast_router(gast_boolOp_and, "js"))

    def test_boolOp_or_and_py (self):
        self.assertEqual('True or False and 4', gtc.gast_router(gast_boolOp_or_and, "py"))

    def test_boolOp_or_and_js (self):
        self.assertEqual('true || false && 4', gtc.gast_router(gast_boolOp_or_and, "js"))

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


if __name__ == '__main__':
    unittest2.main()