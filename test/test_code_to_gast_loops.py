import unittest2
import sys
 
sys.path.append('code_to_gast')
sys.path.append('code_to_gast/assign')
sys.path.append('code_to_gast/expression')
sys.path.append('code_to_gast/conditional')
sys.path.append('code_to_gast/loop')
sys.path.append('code_to_gast/helpers')
sys.path.append('code_to_gast/routers')

import py_main
import js_main


class test_code_to_gast_loops(unittest2.TestCase):
    maxDiff = None
    def test_forRange(self):
        js_input = 'for (let i = 0; i < 10; i += 2) {\n\t5\n}'
        py_input = 'for i in range (0, 10, 2):\n\t5'
        
        expected_gast = {
            "type": "forRangeStatement",
            "init": 
            {
                "type": "varAssign",
                "kind": "let",
                "varId":
                {
                    "type": "name",
                    "value": "i"
                },
                "varValue":
                {
                    "type": "num",
                    "value": 0
                }

            },
            "test": 
            {
                "type": "binOp",
                "left": 
                {
                    "type": "name",
                    "value": "i"
                },
                "op": "<",
                "right": 
                {
                    "type": "num",
                    "value": 10
                }
            },
            "update": 
            {
                "type": "augAssign",
                "left":
                {
                    "type": "name",
                    "value": "i"
                },
                "op": "+=",
                "right": 
                {
                    "type": "num",
                    "value": 2
                }
            },
            "body": 
            [
                {
                    "type": "num",
                    "value": 5
                }
            ]
        }

        self.assertEqual(expected_gast, py_main.py_to_gast(py_input))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_input))

    def test_forOf(self):
        js_input = 'for (elem of [1, 2]) {\n\t5\n}'
        py_input = 'for elem in [1, 2]:\n\t5'
        
        expected_gast = {
            "type": "forOfStatement",
            "init":  
            {
                "type": "name",
                "value": "elem"
            },
            "iter": 
            {
                "type": "arr",
                "elements":
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
            },
            "body": 
            [
                {
                    "type": "num",
                    "value": 5
                }
            ]
        }

        self.assertEqual(expected_gast, py_main.py_to_gast(py_input))
        self.assertEqual(expected_gast, js_main.js_to_gast(js_input))


if __name__ == '__main__':
    unittest2.main()
    