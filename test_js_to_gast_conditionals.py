import unittest2
import sys

sys.path.append('translate')
sys.path.append('translate/assign')
sys.path.append('translate/expression')
sys.path.append('translate/conditional')
sys.path.append('translate/helpers')
sys.path.append('translate/routers')

import js_main


class test_js_to_gast_conditionals(unittest2.TestCase):
    def test_ifs(self):
        js_code = 'if (true) {\n\tconsole.log("This is true")\n}'
        expected_gast = {
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
        self.assertEqual(expected_gast, js_main.js_to_gast(js_code))

    def test_else(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}' # TODO: consider adding ; after console.log()
        expected_gast = {
            'type': 'root', 
            'body': [{
                'type': 'if',
                'body': [{
                     'type': 'logStatement', 
                     'args': [{'type': 'str', 'value': '1 is true'}]
                     }], 
                'orelse': [{
                         'type': 'logStatement',
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
                    'type': 'logStatement', 
                    'args': [{'type': 'str', 'value': '1 is true'}]
                    }], 
                'orelse': [{
                    'type': 'if', 
                    'body': [
                        {
                        'type': 'logStatement', 
                        'args': [{'type': 'str', 'value': '1 is NOT true'}]
                        },
                        {
                        'type': 'logStatement', 
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