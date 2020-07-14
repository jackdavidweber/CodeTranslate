import unittest2
import main

class TestBashPrimitives(unittest2.TestCase):
    def test_boolean(self):
        js_code = 'true'
        bash_code = 'true'
        py_code = 'True'
        self.assertEqual(py_code, main.main(bash_code, 'bash', 'py'))
        self.assertEqual(bash_code, main.main(js_code, 'js', 'bash'))

    def test_string(self):
        js_code = '"hello"'
        bash_code = '"hello"'
        py_code = '"hello"'
        self.assertEqual(py_code, main.main(bash_code, 'bash', 'py'))
        self.assertEqual(bash_code, main.main(js_code, 'js', 'bash'))
    
    def test_number(self):
        js_code = '46'
        bash_code = '46'
        py_code = '46'
        self.assertEqual(py_code, main.main(bash_code, 'bash', 'py'))
        self.assertEqual(bash_code, main.main(js_code, 'js', 'bash'))
    
    


if __name__ == '__main__':
    unittest2.main()