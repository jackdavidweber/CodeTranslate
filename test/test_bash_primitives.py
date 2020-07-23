import unittest2
import translate


class TestBashPrimitives(unittest2.TestCase):

    def test_string(self):
        js_code = '"hello"'
        bash_code = '"hello"'
        py_code = '"hello"'
        self.assertEqual(bash_code, translate.translate(py_code, 'py', 'bash'))
        self.assertEqual(bash_code, translate.translate(js_code, 'js', 'bash'))

    def test_number(self):
        js_code = '46'
        bash_code = '46'
        py_code = '46'
        self.assertEqual(bash_code, translate.translate(py_code, 'py', 'bash'))
        self.assertEqual(bash_code, translate.translate(js_code, 'js', 'bash'))

    def test_arr(self):
        self.assertEqual('(1, 2)', translate.translate('[1, 2]', 'py', 'bash'))


if __name__ == '__main__':
    unittest2.main()
