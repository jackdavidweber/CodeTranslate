import unittest2
import matrix
from Unittest import Unittest


class TestBinBoolOps(unittest2.TestCase):

    def test_bin_no_nesting(self):
        py_code = Unittest('1 + 2', 'py', True, True)
        js_code = Unittest('1 + 2', 'js', True, True)
        java_code = Unittest('1 + 2;', 'java', False, True)
        bash_code = Unittest('1 + 2', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_bin_left_nesting(self):
        py_code = Unittest('1 + 2 + 3', 'py', True, True)
        js_code = Unittest('1 + 2 + 3', 'js', True, True)
        java_code = Unittest('1 + 2 + 3;', 'java', False, True)
        bash_code = Unittest('1 + 2 + 3', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_bin_right_nesting(self):
        py_code = Unittest('1 + 2 * 3', 'py', True, True)
        js_code = Unittest('1 + 2 * 3', 'js', True, True)
        java_code = Unittest('1 + 2 * 3;', 'java', False, True)
        bash_code = Unittest('1 + 2 * 3', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_bin_both_nesting(self):
        py_code = Unittest('1 * 2 + 3 * 4', 'py', True, True)
        js_code = Unittest('1 * 2 + 3 * 4', 'js', True, True)
        java_code = Unittest('1 * 2 + 3 * 4;', 'java', False, True)
        bash_code = Unittest('1 * 2 + 3 * 4', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_bin_multilevel_nesting(self):
        py_code = Unittest('1 * 2 - 4 / 3 * 4 * 5', 'py', True, True)
        js_code = Unittest('1 * 2 - 4 / 3 * 4 * 5', 'js', True, True)
        java_code = Unittest('1 * 2 - 4 / 3 * 4 * 5;', 'java', False, True)
        bash_code = Unittest('1 * 2 - 4 / 3 * 4 * 5', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_bool_no_nesting(self):
        py_code = Unittest('True and True', 'py', True, True)
        js_code = Unittest('true && true', 'js', True, True)
        matrix.matrix(self, [py_code, js_code])

    def test_bool_left_nesting(self):
        py_code = Unittest('True and True or False', 'py', True, True)
        js_code = Unittest('true && true || false', 'js', True, True)
        matrix.matrix(self, [py_code, js_code])

    def test_bool_no_nesting_py(self):
        py_code = Unittest('1 or 2 or 3 or 4 or 5', 'py', True, True)
        js_code = Unittest('1 || 2 || 3 || 4 || 5', 'js', True, True)
        matrix.matrix(self, [py_code, js_code])

    def test_bool_right_nesting(self):
        py_code = Unittest('True or True and False', 'py', True, True)
        js_code = Unittest('true || true && false', 'js', True, True)
        matrix.matrix(self, [py_code, js_code])

    def test_bool_nesting_no_nest_combo(self):
        py_code = Unittest('1 or 2 or 3 or 4 and 6', 'py', True, True)
        js_code = Unittest('1 || 2 || 3 || 4 && 6', 'js', True, True)
        matrix.matrix(self, [py_code, js_code])

    def test_bool_bin_combo(self):
        py_code = Unittest('1 or 2 + 3', 'py', True, True)
        js_code = Unittest('1 || 2 + 3', 'js', True, True)
        matrix.matrix(self, [py_code, js_code])

    def test_combo_nested(self):
        py_code = Unittest('1 or 2 and 3 or 4 + 3', 'py', True, True)
        js_code = Unittest('1 || 2 && 3 || 4 + 3', 'js', True, True)
        matrix.matrix(self, [py_code, js_code])

    def test_compare_greater_than(self):
        py_code = Unittest('1 > 2', 'py', True, True)
        js_code = Unittest('1 > 2', 'js', True, True)
        java_code = Unittest('1 > 2;', 'java', False, True)
        bash_code = Unittest('1 > 2', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_compare_less_than_or_equal(self):
        py_code = Unittest('1 <= 2', 'py', True, True)
        js_code = Unittest('1 <= 2', 'js', True, True)
        java_code = Unittest('1 <= 2;', 'java', False, True)
        bash_code = Unittest('1 <= 2', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_compare_equal(self):
        py_code = Unittest('1 == 2', 'py', True, True)
        js_code = Unittest('1 == 2', 'js', True, True)
        java_code = Unittest('1 == 2;', 'java', False, True)
        bash_code = Unittest('1 == 2', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_comparemulti_equal(self):
        py_code = Unittest('1 == 2 == 3', 'py', True, True)
        js_code = Unittest('1 == 2 == 3', 'js', True, True)
        java_code = Unittest('1 == 2 == 3;', 'java', False, True)
        bash_code = Unittest('1 == 2 == 3', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_comparemulti_all_ops(self):
        py_code = Unittest('1 < 2 <= 3 == 4 >= 5 > 6', 'py', True, True)
        js_code = Unittest('1 < 2 <= 3 == 4 >= 5 > 6', 'js', True, True)
        java_code = Unittest('1 < 2 <= 3 == 4 >= 5 > 6;', 'java', False, True)
        bash_code = Unittest('1 < 2 <= 3 == 4 >= 5 > 6', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_comparemulti_strs(self):
        py_code = Unittest('a > b >= c == C', 'py', True, True)
        js_code = Unittest('a > b >= c == C', 'js', True, True)
        java_code = Unittest('a > b >= c == C;', 'java', False, True)
        bash_code = Unittest('a > b >= c == C', 'bash', False, True)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])


if __name__ == '__main__':
    unittest2.main()
