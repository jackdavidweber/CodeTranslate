import unittest2
import matrix
import translate


class TestPrimitives(unittest2.TestCase):

    def test_string(self):
        js_code = '"hello"'
        bash_code = '"hello"'
        py_code = '"hello"'
        java_code = '"hello";'
        matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_number(self):
        js_code = '46'
        bash_code = '46'
        py_code = '46'
        java_code = '46;'
        matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_array(self):
        py_code = "[1, 2]"
        js_code = "[1, 2]"
        java_code = "{1, 2};"
        bash_code = "(1, 2)"
        matrix.test(self, py_code, js_code)
        self.assertEqual(java_code, translate.translate(js_code, 'js', 'java'))
        self.assertEqual(bash_code, translate.translate(py_code, 'py', 'bash'))


if __name__ == '__main__':
    unittest2.main()
