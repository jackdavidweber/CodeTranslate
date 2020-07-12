import unittest2
import gast_to_code.gast_to_code_router as gtc


class TestGastToCodeIndentation(unittest2.TestCase):

    def test_indent_if (self):
        input_gast = {
            'type': 'root', 
            'body': [
                {
                    'type': 'if', 
                    'body': [
                        {
                            'type': 'if', 
                            'body': [
                                {
                                    'type': 'funcCall', 
                                    'value': {
                                        'type': 'logStatement'
                                    }, 
                                    'args': [
                                        {
                                            'type': 'str', 
                                            'value': 'y and x are true'
                                        }
                                    ]
                                }
                            ],
                            'orelse': [], 
                            'test': {
                                'type': 'binOp', 
                                'left': {'type': 'name', 'value': 'y'}, 
                                'op': '==', 
                                'right': {'type': 'bool', 'value': 1}
                            }
                        }
                    ], 
                    'orelse': [], 
                    'test': {
                        'type': 'binOp', 
                        'left': {'type': 'name', 'value': 'x'}, 
                        'op': '==', 
                        'right': {'type': 'bool', 'value': 1}
                    }
                }
            ]
        }

        expected_js = 'if (x == true) {\n\tif (y == true) {\n\t\tconsole.log("y and x are true")\n\t}\n}'
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js"))

        expected_py = 'if (x == True):\n\tif (y == True):\n\t\tprint("y and x are true")'
        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py"))

    def test_indent_for_of(self):
        input_gast = {'type': 'root', 'body': [{'type': 'forOfStatement', 'init': {'type': 'name', 'value': 'j'}, 'iter': {'type': 'arr', 'elements': [{'type': 'num', 'value': 1}, {'type': 'num', 'value': 2}]}, 'body': [{'type': 'forOfStatement', 'init': {'type': 'name', 'value': 'k'}, 'iter': {'type': 'arr', 'elements': [{'type': 'num', 'value': 3}, {'type': 'num', 'value': 4}]}, 'body': [{'type': 'name', 'value': 'j'}, {'type': 'name', 'value': 'k'}]}]}]}

        expected_js = 'for (j of [1, 2]) {\n\tfor (k of [3, 4]) {\n\t\tj\n\t\tk\n\t}\n}'
        self.assertEqual(expected_js, gtc.gast_to_code(input_gast, "js"))

        expected_py = 'for j in [1, 2]:\n\tfor k in [3, 4]:\n\t\tj\n\t\tk'
        self.assertEqual(expected_py, gtc.gast_to_code(input_gast, "py"))

if __name__ == '__main__':
    unittest2.main()