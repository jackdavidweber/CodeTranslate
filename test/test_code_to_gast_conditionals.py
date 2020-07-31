import unittest2
import python.code_to_gast.py_main as py_main
import javascript.code_to_gast.js_main as js_main
import java.code_to_gast.java_main as java_main


class test_code_to_gast_conditionals(unittest2.TestCase):
    maxDiff = None

    def test_ifs(self):
        py_code = 'if (True):\n\tprint("This is true")'
        js_code = 'if (true) {\n\tconsole.log("This is true")\n}'
        java_code = 'if (true) {System.out.println("This is true");}'
        expected_gast = {
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
        self.assertEqual(expected_gast, py_main.py_to_gast(py_code))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_code))
        self.assertEqual(expected_gast, java_main.java_to_gast(java_code))

    def test_else(self):
        py_code = 'if (1):\n\tprint("1 is true")\nelse:\n\tprint("1 is NOT true")\n'
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}'  # TODO: consider adding ; after console.log()
        java_code = 'if (1) {System.out.println("1 is true");} else {System.out.println("1 is NOT true");}'
        expected_gast = {
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
        self.assertEqual(expected_gast, py_main.py_to_gast(py_code))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_code))
        self.assertEqual(expected_gast, java_main.java_to_gast(java_code))

    def test_elif(self):
        py_code = 'if (1):\n\tprint("1 is true")\nelif (2):\n\tprint("2 is true")\n\tprint("second line")\n'
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'
        java_code = 'if (1) {System.out.println("1 is true");} else if (2) {System.out.println("2 is true"); System.out.println("second line");}'
        expected_gast = {
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
        self.assertEqual(expected_gast, py_main.py_to_gast(py_code))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_code))
        self.assertEqual(expected_gast, java_main.java_to_gast(java_code))

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

        self.assertEqual(expected_gast, py_main.py_to_gast(py_input))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_input))
        self.assertEqual(expected_gast, java_main.java_to_gast(java_input))

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

        self.assertEqual(expected_gast, py_main.py_to_gast(py_input))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_input))
        self.assertEqual(expected_gast, java_main.java_to_gast(java_input))

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

        self.assertEqual(expected_gast, py_main.py_to_gast(py_input))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_input))

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

        self.assertEqual(expected_gast, py_main.py_to_gast(py_input))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_input))
        self.assertEqual(expected_gast, java_main.java_to_gast(java_input))

if __name__ == '__main__':
    unittest2.main()
