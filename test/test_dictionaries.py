import sys

sys.path.append('../cjs_capstone')

import unittest2
import main

class TestDictionaries(unittest2.TestCase):
    def test_assignment(self):
        js_code = 'let d = {1: 2}'
        py_code = 'd = {1: 2}'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_print(self):
        js_code = 'console.log({"first": true})'
        py_code = 'print({"first": True})'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    
    def test_function(self):
        js_code = 'my.function({"4": 1 + 1})'
        py_code = 'my.function({"4": 1 + 1})'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()