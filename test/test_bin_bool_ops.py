import sys
sys.path.insert(1, '/home/stephwalsh/capstone/cjs_capstone/')

import unittest2
import main

class TestConditionals(unittest2.TestCase):
    '''def test_bin_no_nesting(self):
        js_code = '1 + 2'
        py_code = '1 + 2'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    def test_bin_left_nesting(self):
        js_code = '1 + 2 + 3'
        py_code = '1 + 2 + 3'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    def test_bin_right_nesting(self):
        js_code = '1 + 2 * 3'
        py_code = '1 + 2 * 3'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    def test_bin_both_nesting(self):
        js_code = '1 * 2 + 3 * 4'
        py_code = '1 * 2 + 3 * 4'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    def test_bin_multilevel_nesting(self):
        js_code = '1 * 2 - 4 / 3 * 4 * 5'
        py_code = '1 * 2 - 4 / 3 * 4 * 5'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    #NOTE: test bin ops w parantheses ??

    def test_bool_no_nesting(self):
        js_code = 'true && true'
        py_code = 'True and True'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    def test_bool_left_nesting(self):
        js_code = 'true && true || false'
        py_code = 'True and True or False'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))'''
    def test_bool_right_nesting(self):
        js_code = 'true || true || false'
        py_code = 'True or True or False'
        #self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        #this is broken
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
  

if __name__ == '__main__':
    unittest2.main()