import unittest2
import main


class TestBashPrimitives(unittest2.TestCase):

    def test_string(self):
        js_code = '"hello"'
        bash_code = '"hello"'
        py_code = '"hello"'
        self.assertEqual(bash_code, main.main(py_code, 'py', 'bash'))
        self.assertEqual(bash_code, main.main(js_code, 'js', 'bash'))

    def test_number(self):
        js_code = '46'
        bash_code = '46'
        py_code = '46'
        self.assertEqual(bash_code, main.main(py_code, 'py', 'bash'))
        self.assertEqual(bash_code, main.main(js_code, 'js', 'bash'))

    def test_arr(self):
        self.assertEqual('(1, 2)', main.main('[1, 2]', 'py', 'bash'))


if __name__ == '__main__':
    unittest2.main()
