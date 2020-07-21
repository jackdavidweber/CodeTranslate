import unittest2
import shared.gast_to_code.gast_to_code_router as gtc


class TestGastToCode(unittest2.TestCase):
    # test primitives
    def test_primitive_str(self):
        gast_str = {"type": "str", "value": "hello world"}

        self.assertEqual('"hello world"', gtc.gast_to_code(gast_str, "py")['translation']['output_code'])
        self.assertEqual('"hello world"', gtc.gast_to_code(gast_str, "js")['translation']['output_code'])

    def test_primitive_num(self):
        gast_num = {"type": "num", "value": 47.47}

        self.assertEqual('47.47', gtc.gast_to_code(gast_num, "py")['translation']['output_code'])
        self.assertEqual('47.47', gtc.gast_to_code(gast_num, "js")['translation']['output_code'])

    def test_primitive_true(self):
        gast_true = {"type": "bool", "value": 1}

        self.assertEqual('True', gtc.gast_to_code(gast_true, "py")['translation']['output_code'])
        self.assertEqual('true', gtc.gast_to_code(gast_true, "js")['translation']['output_code'])

    def test_primitive_false(self):
        gast_false = {"type": "bool", "value": 0}

        self.assertEqual('false', gtc.gast_to_code(gast_false, "js")['translation']['output_code'])
        self.assertEqual('False', gtc.gast_to_code(gast_false, "py")['translation']['output_code'])

    # test other types
    def test_nested_arr(self):
        gast_arr = {
            "type":
                "arr",
            "elements": [{
                "type": "str",
                "value": "hello"
            }, {
                "type":
                    "arr",
                "elements": [{
                    "type": "num",
                    "value": 1
                }, {
                    "type": "num",
                    "value": 2
                }]
            }]
        }

        self.assertEqual('["hello", [1, 2]]', gtc.gast_to_code(gast_arr, "py")['translation']['output_code'])
        self.assertEqual('["hello", [1, 2]]', gtc.gast_to_code(gast_arr, "js")['translation']['output_code'])

    def test_binOp_add(self):
        gast_binOp_add = {
            'type': 'binOp',
            'op': '+',
            'left': {
                'type': 'num',
                'value': 3
            },
            'right': {
                'type': 'num',
                'value': 4
            }
        }

        self.assertEqual('3 + 4', gtc.gast_to_code(gast_binOp_add, "py")['translation']['output_code'])
        self.assertEqual('3 + 4', gtc.gast_to_code(gast_binOp_add, "js")['translation']['output_code'])

    def test_binOp_bitwise(self):
        gast_binOp_bitwise = {
            'type': 'binOp',
            'op': '&',
            'left': {
                'type': 'num',
                'value': 1
            },
            'right': {
                'type': 'num',
                'value': 3
            }
        }

        self.assertEqual('1 & 3', gtc.gast_to_code(gast_binOp_bitwise, "py")['translation']['output_code'])
        self.assertEqual('1 & 3', gtc.gast_to_code(gast_binOp_bitwise, "js")['translation']['output_code'])

    def test_binOp_add_sub_mult_div(self):
        gast_binOp_add_sub_mult_div = {
            'type': 'binOp',
            'op': '-',
            'left': {
                'type': 'binOp',
                'op': '+',
                'left': {
                    'type': 'num',
                    'value': 1
                },
                'right': {
                    'type': 'num',
                    'value': 2
                }
            },
            'right': {
                'type': 'binOp',
                'op': '/',
                'left': {
                    'type': 'binOp',
                    'op': '*',
                    'left': {
                        'type': 'num',
                        'value': 3
                    },
                    'right': {
                        'type': 'num',
                        'value': 4
                    }
                },
                'right': {
                    'type': 'num',
                    'value': 5
                }
            }
        }

        self.assertEqual('1 + 2 - 3 * 4 / 5',
                         gtc.gast_to_code(gast_binOp_add_sub_mult_div, "py")['translation']['output_code'])
        self.assertEqual('1 + 2 - 3 * 4 / 5',
                         gtc.gast_to_code(gast_binOp_add_sub_mult_div, "js")['translation']['output_code'])

    def test_boolOp_and(self):
        gast_boolOp_and = {
            'type': 'boolOp',
            'op': '&&',
            'left': {
                'type': 'bool',
                'value': 1
            },
            'right': {
                'type': 'bool',
                'value': 0
            }
        }

        self.assertEqual('True and False',
                         gtc.gast_to_code(gast_boolOp_and, "py")['translation']['output_code'])
        self.assertEqual('true && false',
                         gtc.gast_to_code(gast_boolOp_and, "js")['translation']['output_code'])

    def test_boolOp_or_and(self):
        gast_boolOp_or_and = {
            'type': 'boolOp',
            'op': '||',
            'left': {
                'type': 'bool',
                'value': 1
            },
            'right': {
                'type': 'boolOp',
                'op': '&&',
                'left': {
                    'type': 'bool',
                    'value': 0
                },
                'right': {
                    'type': 'num',
                    'value': 4
                }
            }
        }

        self.assertEqual('True or False and 4',
                         gtc.gast_to_code(gast_boolOp_or_and, "py")['translation']['output_code'])
        self.assertEqual('true || false && 4',
                         gtc.gast_to_code(gast_boolOp_or_and, "js")['translation']['output_code'])

    # test logStatement
    def test_logStatement_bool(self):
        gast_logStatement_bool = {
            "type":
                "root",
            "body": [{
                "type": "funcCall",
                "args": [{
                    "type": "bool",
                    "value": 0
                }],
                "value": {
                    "type": "logStatement"
                }
            }]
        }

        self.assertEqual('print(False)',
                         gtc.gast_to_code(gast_logStatement_bool, "py")['translation']['output_code'])
        self.assertEqual('console.log(false)',
                         gtc.gast_to_code(gast_logStatement_bool, "js")['translation']['output_code'])

    def test_js_logStatement_two_arguments(self):
        gast_logStatement = {
            "type":
                "root",
            "body": [{
                "type": "funcCall",
                "args": [{
                    "type": "str",
                    "value": "hello world"
                }, {
                    "type": "num",
                    "value": 5
                }],
                "value": {
                    "type": "logStatement"
                }
            }]
        }
        self.assertEqual('print("hello world", 5)',
                         gtc.gast_to_code(gast_logStatement, "py")['translation']['output_code'])
        self.assertEqual('console.log("hello world", 5)',
                         gtc.gast_to_code(gast_logStatement, "js")['translation']['output_code'])

    # test varAssign
    def test_js_varAssign_let(self):
        gast_varAssign_let = {
            "type":
                "root",
            "body": [{
                "type": "varAssign",
                "kind": "let",
                "varId": {
                    "type": "name",
                    "value": "x"
                },
                "varValue": {
                    "type": "num",
                    "value": 5
                }
            },]
        }

        self.assertEqual('x = 5', gtc.gast_to_code(gast_varAssign_let, "py")['translation']['output_code'])
        self.assertEqual('let x = 5', gtc.gast_to_code(gast_varAssign_let,
                                                       "js"))

    def test_js_varAssign_const(self):
        gast_varAssign_const = {
            "type":
                "root",
            "body": [{
                "type": "varAssign",
                "kind": "const",
                "varId": {
                    "type": "name",
                    "value": "x"
                },
                "varValue": {
                    "type": "num",
                    "value": 5
                }
            },]
        }

        self.assertEqual('x = 5', gtc.gast_to_code(gast_varAssign_const, "py")['translation']['output_code'])
        self.assertEqual('const x = 5',
                         gtc.gast_to_code(gast_varAssign_const, "js")['translation']['output_code'])

    # test multiple items in body
    def test_multi_body(self):
        gast_multi_body = {
            "type":
                "root",
            "body": [
                {
                    "type": "varAssign",
                    "kind": "const",
                    "varId": {
                        "type": "name",
                        "value": "x"
                    },
                    "varValue": {
                        "type": "num",
                        "value": 5
                    }
                },
                {
                    "type": "varAssign",
                    "kind": "const",
                    "varId": {
                        "type": "name",
                        "value": "x"
                    },
                    "varValue": {
                        "type": "num",
                        "value": 5
                    }
                },
            ]
        }
        self.assertEqual('x = 5\nx = 5',
                         gtc.gast_to_code(gast_multi_body, "py")['translation']['output_code'])

    def test_if(self):
        input_gast = {
            'type':
                'root',
            'body': [{
                'type': 'if',
                'body': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': 'This is true'
                    }]
                }],
                'orelse': [],
                'test': {
                    'type': 'bool',
                    'value': 1
                }
            }]
        }
        expected_js = 'if (true) {\n\tconsole.log("This is true")\n}'
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js")['translation']['output_code'])

        expected_py = 'if (True):\n\tprint("This is true")'
        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py")['translation']['output_code'])

    def test_else(self):
        input_gast = {
            'type':
                'root',
            'body': [{
                'type': 'if',
                'body': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': '1 is true'
                    }]
                }],
                'orelse': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': '1 is NOT true'
                    }]
                }],
                'test': {
                    'type': 'num',
                    'value': 1
                }
            }]
        }

        expected_js = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}'  # TODO: consider adding ; after console.log()
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js")['translation']['output_code'])

        expected_py = 'if (1):\n\tprint("1 is true")\nelse:\n\tprint("1 is NOT true")'
        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py")['translation']['output_code'])

    def test_elif(self):
        input_gast = {
            'type':
                'root',
            'body': [{
                'type': 'if',
                'body': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': '1 is true'
                    }]
                }],
                'orelse': [{
                    'type': 'if',
                    'body': [{
                        'type': 'funcCall',
                        'value': {
                            'type': 'logStatement'
                        },
                        'args': [{
                            'type': 'str',
                            'value': '2 is true'
                        }]
                    }, {
                        'type': 'funcCall',
                        'value': {
                            'type': 'logStatement'
                        },
                        'args': [{
                            'type': 'str',
                            'value': 'second line'
                        }]
                    }],
                    'orelse': [],
                    'test': {
                        'type': 'num',
                        'value': 2
                    }
                }],
                'test': {
                    'type': 'num',
                    'value': 1
                }
            }]
        }

        expected_py = 'if (1):\n\tprint("1 is true")\nelif (2):\n\tprint("2 is true")\n\tprint("second line")'
        expected_js = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'

        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py")['translation']['output_code'])
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js")['translation']['output_code'])

    def test_forRange(self):
        input_gast = {
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
        }

        expected_js = 'for (let i = 0; i < 10; i += 2) {\n\t5\n}'
        expected_py = 'for i in range (0, 10, 2):\n\t5'

        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py")['translation']['output_code'])
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js")['translation']['output_code'])

    def test_forOf(self):
        input_gast = {
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
        }

        expected_js = 'for (elem of [1, 2]) {\n\t5\n}'
        expected_py = 'for elem in [1, 2]:\n\t5'

        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py")['translation']['output_code'])
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js")['translation']['output_code'])


if __name__ == '__main__':
    unittest2.main()
