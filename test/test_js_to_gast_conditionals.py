import sys
import unittest2

sys.path.append('code_to_gast')
sys.path.append('code_to_gast/assign')
sys.path.append('code_to_gast/expression')
sys.path.append('code_to_gast/conditional')
sys.path.append('code_to_gast/helpers')
sys.path.append('code_to_gast/routers')

import js_main


class test_js_to_gast_conditionals(unittest2.TestCase):
    maxDiff = None
    def test_ifs(self):
        js_code = 'if (true) {\n\tconsole.log("This is true")\n}'
        expected_gast = {
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
        self.assertEqual(expected_gast, js_main.js_to_gast(js_code))

    def test_else(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}' # TODO: consider adding ; after console.log()
        expected_gast = {
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
        self.assertEqual(expected_gast, js_main.js_to_gast(js_code))
   
    def test_elif(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'
        expected_gast = {
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
        self.assertEqual(expected_gast, js_main.js_to_gast(js_code))

if __name__ == '__main__':
    unittest2.main()