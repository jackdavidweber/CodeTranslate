import unittest2
import matrix
from Unittest import Unittest


class TestVarAssign(unittest2.TestCase):

    def test_string_assign(self):
        py_code = Unittest('x = "hi"', 'py')
        js_code = Unittest('let x = "hi"', 'js')
        java_code = Unittest('String x = "hi";', 'java')
        bash_code = Unittest('x = "hi"', 'bash', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_int_assign(self):
        py_code = Unittest('num = 109', 'py')
        js_code = Unittest('let num = 109', 'js')
        java_code = Unittest('int num = 109;', 'java')
        bash_code = Unittest('num = 109', 'bash', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_array_assign(self):
        py_code = Unittest('arr = [3, 6]', 'py')
        js_code = Unittest('let arr = [3, 6]', 'js')
        java_code = Unittest('int[] arr = {3, 6};', 'java')
        bash_code = Unittest('arr = (3, 6)', 'bash', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_nested_array_assign(self):
        py_code = Unittest('arr = [[1, 9], [2, 8]]', 'py')
        js_code = Unittest('let arr = [[1, 9], [2, 8]]', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_boolean_assign(self):
        py_code = Unittest('boo = True', 'py')
        js_code = Unittest('let boo = true', 'js')
        java_code = Unittest('boolean boo = true;', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_none_assign(self):
        py_code = Unittest('no = None', 'py')
        js_code = Unittest('let no = null', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_aug_assign_minus(self):
        py_code = Unittest('x -= 1', 'py')
        js_code = Unittest('x -= 1', 'js')
        java_code = Unittest('x -= 1;', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_aug_assign_mult(self):
        py_code = Unittest('hi *= 5', 'py')
        js_code = Unittest('hi *= 5', 'js')
        java_code = Unittest('hi *= 5;', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_update_expression(self):
        py_code = Unittest('x += 1', 'py', is_input=False)
        js_code = Unittest('x++', 'js')
        java_code = Unittest('x++;', 'java')
        bash_code = Unittest('x++', 'bash', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])


if __name__ == '__main__':
    unittest2.main()
