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

if __name__ == '__main__':
    unittest2.main()