import unittest2
import matrix
import translate
from Unittest import Unittest


class TestPrimitives(unittest2.TestCase):

    def test_string(self):
        js_code = Unittest('"hello"', "js", True, True)
        bash_code = Unittest('"hello"', "bash", False, True)
        py_code = Unittest('"hello"', "py", True, True)
        java_code = Unittest('"hello";', "java", True, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_number(self):
        js_code = Unittest('46', "js", True, True)
        bash_code = Unittest('46', "bash", False, True)
        py_code = Unittest('46', "py", True, True)
        java_code = Unittest('46;', "java", True, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_array(self):
        js_code = Unittest('[1, 2]', "js", True, True)
        bash_code = Unittest('(1, 2)', "bash", False, True)
        py_code = Unittest('[1, 2]', "py", True, True)
        java_code = Unittest('{1, 2};', "java", False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])


if __name__ == '__main__':
    unittest2.main()
