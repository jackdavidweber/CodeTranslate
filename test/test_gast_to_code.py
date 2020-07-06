import sys

sys.path.append('../cjs_capstone')

import unittest2
import gast_to_code.gast_to_code_main as gtc


class TestGastToCode(unittest2.TestCase):
    # test primitives
    def test_primitive_str(self):
        gast_str = { "type": "str", "value": "hello world" }

        self.assertEqual('"hello world"', gtc.gast_to_code(gast_str, "py"))
        self.assertEqual('"hello world"', gtc.gast_to_code(gast_str, "js"))

    def test_primitive_num(self):
        gast_num = { "type": "num", "value": 47.47 }

        self.assertEqual('47.47', gtc.gast_to_code(gast_num,"py"))
        self.assertEqual('47.47', gtc.gast_to_code(gast_num,"js"))

    def test_primitive_true (self):
        gast_true = {"type": "bool", "value": 1}

        self.assertEqual('True', gtc.gast_to_code(gast_true, "py"))
        self.assertEqual('true', gtc.gast_to_code(gast_true, "js"))

    def test_primitive_false (self):
        gast_false = {"type": "bool", "value": 0}

        self.assertEqual('false', gtc.gast_to_code(gast_false, "js"))
        self.assertEqual('False', gtc.gast_to_code(gast_false, "py"))

    # test other types
    def test_nested_arr(self):
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

        self.assertEqual('["hello", [1, 2]]', gtc.gast_to_code(gast_arr, "py"))
        self.assertEqual('["hello", [1, 2]]', gtc.gast_to_code(gast_arr, "js"))

    def test_binOp_add (self):
        gast_binOp_add = {'type': 'binOp', 'op': '+', 'left': {'type': 'num', 'value': 3}, 'right': {'type': 'num', 'value': 4}}

        self.assertEqual('3 + 4', gtc.gast_to_code(gast_binOp_add, "py"))
        self.assertEqual('3 + 4', gtc.gast_to_code(gast_binOp_add, "js"))

    def test_binOp_bitwise (self):
        gast_binOp_bitwise = {'type': 'binOp', 'op': '&', 'left': {'type': 'num', 'value': 1}, 'right': {'type': 'num', 'value': 3}}

        self.assertEqual('1 & 3', gtc.gast_to_code(gast_binOp_bitwise, "py"))
        self.assertEqual('1 & 3', gtc.gast_to_code(gast_binOp_bitwise, "js"))

    def test_binOp_add_sub_mult_div (self):
        gast_binOp_add_sub_mult_div = {'type': 'binOp', 'op': '-', 'left': {'type': 'binOp', 'op': '+', 'left': {'type': 'num', 'value': 1}, 'right': {'type': 'num', 'value': 2}}, 'right': {'type': 'binOp', 'op': '/', 'left': {'type': 'binOp', 'op': '*', 'left': {'type': 'num', 'value': 3}, 'right': {'type': 'num', 'value': 4}}, 'right': {'type': 'num', 'value': 5}}}

        self.assertEqual('1 + 2 - 3 * 4 / 5', gtc.gast_to_code(gast_binOp_add_sub_mult_div, "py"))
        self.assertEqual('1 + 2 - 3 * 4 / 5', gtc.gast_to_code(gast_binOp_add_sub_mult_div, "js"))

    def test_boolOp_and (self):
        gast_boolOp_and = {'type': 'boolOp', 'op': '&&', 'left': {'type': 'bool', 'value': 1}, 'right': {'type': 'bool', 'value': 0}}

        self.assertEqual('True and False', gtc.gast_to_code(gast_boolOp_and, "py"))
        self.assertEqual('true && false', gtc.gast_to_code(gast_boolOp_and, "js"))

    def test_boolOp_or_and (self):
        gast_boolOp_or_and = {'type': 'boolOp', 'op': '||', 'left': {'type': 'bool', 'value': 1}, 'right': {'type': 'boolOp', 'op': '&&', 'left': {'type': 'bool', 'value': 0}, 'right': {'type': 'num', 'value': 4}}}

        self.assertEqual('True or False and 4', gtc.gast_to_code(gast_boolOp_or_and, "py"))
        self.assertEqual('true || false && 4', gtc.gast_to_code(gast_boolOp_or_and, "js"))

    # test logStatement
    def test_logStatement_bool (self):
        gast_logStatement_bool = {
            "type": "root",
            "body": [
                {
                    "type": "funcCall",
                    "args": [
                        {
                            "type": "bool",
                            "value": 0
                        }
                    ],
                    "value": {
                        "type": "logStatement"
                    }
                }
            ]
        }

        self.assertEqual('print(False)', gtc.gast_to_code(gast_logStatement_bool, "py"))
        self.assertEqual('console.log(false)', gtc.gast_to_code(gast_logStatement_bool, "js"))

    def test_js_logStatement_two_arguments(self):
        gast_logStatement = {
            "type": "root",
            "body": [
                {
                    "type": "funcCall",
                    "args": [
                        {
                            "type": "str",
                            "value": "hello world"
                        },
                        {
                            "type": "num",
                            "value": 5
                        }
                    ],
                    "value": {
                        "type": "logStatement"
                    }
                }
            ]
        }
        self.assertEqual('print("hello world", 5)', gtc.gast_to_code(gast_logStatement, "py"))
        self.assertEqual('console.log("hello world", 5)', gtc.gast_to_code(gast_logStatement, "js"))

    # test varAssign
    def test_js_varAssign_let(self):
        gast_varAssign_let = {
            "type": "root",
            "body": [
                {
                    "type": "varAssign",
                    "kind": "let",
                    "varId": {
                        "type": "name",
                        "value": "x"
                    },
                    "varValue": 
                        {
                            "type": "num",
                            "value": 5
                        }
                },
                ]
        }

        self.assertEqual('x = 5', gtc.gast_to_code(gast_varAssign_let, "py"))
        self.assertEqual('let x = 5', gtc.gast_to_code(gast_varAssign_let, "js"))

    def test_js_varAssign_const(self):
        gast_varAssign_const = {
            "type": "root",
            "body": [
                {
                    "type": "varAssign",
                    "kind": "const",
                    "varId": {
                        "type": "name",
                        "value": "x"
                    },
                    "varValue": 
                        {
                            "type": "num",
                            "value": 5
                        }
                },
                ]
        }

        self.assertEqual('x = 5', gtc.gast_to_code(gast_varAssign_const, "py"))
        self.assertEqual('const x = 5', gtc.gast_to_code(gast_varAssign_const, "js"))

    # test multiple items in body
    def test_multi_body (self):
        gast_multi_body = {
            "type": "root",
            "body": [
                { "type": "varAssign", "kind": "const", "varId": {"type": "name", "value": "x"}, "varValue": { "type": "num", "value": 5 } },
                { "type": "varAssign", "kind": "const", "varId": {"type": "name", "value": "x"}, "varValue": { "type": "num", "value": 5 } },
            ]
        }
        self.assertEqual('x = 5\nx = 5', gtc.gast_to_code(gast_multi_body, "py"))

    def test_if (self):
        input_gast = {
            'type': 'root',
            'body': [{
                'type': 'if',
                 'body': [{
                     'type': 'funcCall',
                     'value': {'type': 'logStatement'},
                     'args': [{'type': 'str', 'value': 'This is true'}]
                    }],
                'orelse': [],
                'test': {'type': 'bool', 'value': 1}
                }]
            }
        expected_js = 'if (true) {\n\tconsole.log("This is true")\n}'
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js"))

        expected_py = 'if (True):\n\tprint("This is true")'
        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py"))

    def test_else (self):
        input_gast = {
            'type': 'root', 
            'body': [{
                'type': 'if',
                'body': [{
                     'type': 'funcCall',
                     'value': {'type': 'logStatement'}, 
                     'args': [{'type': 'str', 'value': '1 is true'}]
                     }], 
                'orelse': [{
                         'type': 'funcCall',
                         'value': {'type': 'logStatement'},
                         'args': [{'type': 'str', 'value': '1 is NOT true'}]
                         }], 
                'test': {'type': 'num', 'value': 1}
                }]
            }
        
        expected_js = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}' # TODO: consider adding ; after console.log()
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js"))

        expected_py = 'if (1):\n\tprint("1 is true")\nelse:\n\tprint("1 is NOT true")'
        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py"))

    def test_elif (self):
        input_gast = {
            'type': 'root', 
            'body': [{
                'type': 'if', 
                'body': [{
                    'type': 'funcCall',
                    'value': {'type': 'logStatement'}, 
                    'args': [{'type': 'str', 'value': '1 is true'}]
                    }], 
                'orelse': [{
                    'type': 'if', 
                    'body': [
                        {
                        'type': 'funcCall',
                        'value': {'type': 'logStatement'}, 
                        'args': [{'type': 'str', 'value': '2 is true'}]
                        },
                        {
                        'type': 'funcCall',
                        'value': {'type': 'logStatement'}, 
                        'args': [{'type': 'str', 'value': 'second line'}]
                        }
                    ], 
                    'orelse': [], 
                    'test': {'type': 'num', 'value': 2}
                    }], 
                'test': {'type': 'num', 'value': 1}
                }]
            }     
            
        expected_py = 'if (1):\n\tprint("1 is true")\nelif (2):\n\tprint("2 is true")\n\tprint("second line")'
        expected_js = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'

        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py"))
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js"))


if __name__ == '__main__':
    unittest2.main()