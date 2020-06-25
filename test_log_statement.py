import unittest2
import main

class TestLogStatement(unittest2.TestCase):
    def test_py_to_js_no_args(self):
        self.assertEqual('console.log()', main.main('print()', 'py', 'js'))

    def test_js_to_py_no_args(self):
        self.assertEqual('print()', main.main('console.log()', 'js', 'py'))
    
    def test_one_string_arg(self):
        self.assertEqual('console.log("hello")', main.main('print("hello")', 'py', 'js'))
    
    def test_one_int_arg(self):
        self.assertEqual('print(5)', main.main('console.log(5)', 'js', 'py'))
    
    def test_quotes_string(self):
        self.assertEqual('print("working")', main.main('console.log("working")', 'js', 'py'))
    
    def test_simple_array(self):
        self.assertEqual('console.log(["please", "work"])', main.main('print(["please", "work"])', 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()