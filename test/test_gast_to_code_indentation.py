import unittest2
import gast_to_code.gast_to_code_router as gtc


class TestGastToCodeIndentation(unittest2.TestCase):

    def test_multi_if (self):
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

 

if __name__ == '__main__':
    unittest2.main()