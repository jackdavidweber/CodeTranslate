import unittest2
import main

class TestLogStatement(unittest2.TestCase):
    def test_string_assign_js_to_py(self):
        self.assertEqual('x = "hi"', main.main('let x = "hi"', 'js', 'py'))

    def test_string_assign_py_to_js(self):
        self.assertEqual('const test = "working"', main.main('test = "working"', 'py', 'js'))
    
    def test_int_assign_js_to_py(self):
        self.assertEqual('num = 109', main.main('const num = 109', 'js', 'py'))
    
    def test_int_assign_py_to_js(self):
        self.assertEqual('const n = 12', main.main('n = 12', 'py', 'js'))
    

if __name__ == '__main__':
    unittest2.main()