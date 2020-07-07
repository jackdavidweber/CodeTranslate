import sys

sys.path.append('../cjs_capstone')

import unittest2
import main

class TestLoops(unittest2.TestCase):
    def test_while_simple(self):
        js_code = 'while (true) {\n\t5\n}'
        py_code = 'while (True):\n\t5'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_while_range(self):
        js_code = 'while (x < 10) {\n\t5\n}'
        py_code = 'while (x < 10):\n\t5'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
        
    def test_for_range_increment_two(self):
        js_code = 'for (let i = 0; i < 10; i += 2) {\n\t5\n}'
        py_code = 'for i in range (0,10,2):\n\t5'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_for_inclusiverange_increment_two(self):
        js_code = 'for (let i = 0; i <= 10; i += 2) {\n\t5\n}'
        py_code = 'for i in range (0,12,2):\n\t5'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_for_range_increment_one(self):
        js_code = 'for (let i = 0; i < 10; i += 1) {\n\t5\n}'
        py_code = 'for i in range (0,10):\n\t5'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_for_range_increment_negative(self):
        js_code = 'for (let i = 10; i > 0; i -= 1) {\n\t5\n}'
        py_code = 'for i in range (10,0,-1):\n\t5'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()