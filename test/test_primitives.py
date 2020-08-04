import unittest2
import matrix
from Unittest import Unittest


class TestPrimitives(unittest2.TestCase):

    def test_string(self):
        js_code = Unittest('"hello"', "js")
        bash_code = Unittest('"hello"', "bash", is_input=False)
        py_code = Unittest('"hello"', "py")
        java_code = Unittest('"hello";', "java")
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_number(self):
        js_code = Unittest('46', "js")
        bash_code = Unittest('46', "bash", is_input=False)
        py_code = Unittest('46', "py")
        java_code = Unittest('46;', "java")
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_array(self):
        js_code = Unittest('[1, 2]', "js")
        bash_code = Unittest('(1, 2)', "bash", is_input=False)
        py_code = Unittest('[1, 2]', "py")
        java_code = Unittest('{1, 2};', "java", is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])


if __name__ == '__main__':
    unittest2.main()
