import unittest2
import matrix
from Unittest import Unittest


class TestLoops(unittest2.TestCase):

    def test_while_simple(self):
        js_code = Unittest('while (true) {\n\t5\n}', 'js')
        py_code = Unittest('while (True):\n\t5', 'py')
        java_code = Unittest('while (true) {\n\t5;\n}', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_while_range(self):
        js_code = Unittest('while (x < 10) {\n\t5\n}', 'js')
        py_code = Unittest('while (x < 10):\n\t5', 'py')
        java_code = Unittest('while (x < 10) {\n\t5;\n}', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_range_increment_one(self):
        js_code = Unittest('for (let i = 0; i < 10; i += 1) {\n\t5\n}', 'js')
        py_code = Unittest('for i in range (0, 10, 1):\n\t5', 'py')
        java_code = Unittest('for (int i = 0; i < 10; i += 1) {\n\t5;\n}', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_range_implied_increment_one(self):
        """
        When python's step argument is ommitted, step=1. This test checks
        to make sure functionality is maintained when arg is ommitted.
        """
        js_code = Unittest('for (let i = 0; i < 10; i += 1) {\n\t5\n}', 'js', is_input=False)
        py_code = Unittest('for i in range (0, 10):\n\t5', 'py', is_output=False)
        java_code = Unittest('for (int i = 0; i < 10; i += 1) {\n\t5;\n}', 'java', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_range_increment_two(self):
        js_code = Unittest('for (let i = 0; i < 10; i += 2) {\n\t5\n}', 'js')
        py_code = Unittest('for i in range (0, 10, 2):\n\t5', 'py')
        java_code = Unittest('for (int i = 0; i < 10; i += 2) {\n\t5;\n}', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_inclusiverange_increment_two(self):
        """
        Since python does not have inclusive range, it needs to adjust the end point
        of the range to be effectively inclusive. This test confirms this functionality
        """
        js_code = Unittest('for (let i = 0; i <= 10; i += 2) {\n\t5\n}', 'js', is_output=False)
        py_code = Unittest('for i in range (0, 12, 2):\n\t5', 'py')
        matrix.matrix(self, [py_code, js_code])

    def test_for_with_update_expression_plus(self):
        js_code = Unittest('for (let i = 0; i <= 10; i++) {\n\t5\n}', 'js', is_output=False)
        py_code = Unittest('for i in range (0, 11, 1):\n\t5', 'py')
        java_code = Unittest('for (int i = 0; i <= 10; i++) {\n\t5;\n}', 'java', is_output=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_with_update_expression_minus(self):
        js_code = Unittest('for (let i = 20; i >= -5; i--) {\n\t5\n}', 'js', is_output=False)
        py_code = Unittest('for i in range (20, -4, -1):\n\t5', 'py')
        java_code = Unittest('for (int i = 20; i >= -5; i--) {\n\t5;\n}', 'java', is_output=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_loop_python_incrementor(self):
        js_code = Unittest('for (let i = 0; i < 10; i += 1) {\n\t5\n}', 'js', is_input=False)
        py_code = Unittest('for i in range(0,10,1): \n\t5', 'py', is_output=False)
        java_code = Unittest('for (int i = 0; i < 10; i += 1) {\n\t5;\n}', 'java', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_range_increment_negative(self):
        js_code = Unittest('for (let i = 10; i > 0; i -= 1) {\n\t5\n}', 'js')
        py_code = Unittest('for i in range (10, 0, -1):\n\t5', 'py')
        java_code = Unittest('for (int i = 10; i > 0; i -= 1) {\n\t5;\n}', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_range_all_args_neg(self):
        js_code = Unittest('for (let i = -25; i > -50; i -= 5) {\n\t5\n}', 'js')
        py_code = Unittest('for i in range (-25, -50, -5):\n\t5', 'py')
        java_code = Unittest('for (int i = -25; i > -50; i -= 5) {\n\t5;\n}', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_for_range_one_arg_loop(self):
        ''' 
        users can give range 1 args - translations give range 3 args 
        hence js -> py is not supported for this translation 
        '''
        js_code = Unittest('for (let i = 0; i < 5; i += 1) {\n\tconsole.log(i)\n}', 'js')
        py_code = Unittest('for i in range (5):\n\tprint(i)', 'py', is_output=False)
        java_code = Unittest('for (int i = 0; i < 5; i += 1) {\n\tSystem.out.println(i);\n}', 'java', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_forOf(self):
        js_code = Unittest('for (elem of [1, 2]) {\n\t5\n}', 'js')
        py_code = Unittest('for elem in [1, 2]:\n\t5', 'py')
        java_code = Unittest('for (GenericType elem : {1, 2}) {\n\t5;\n}', 'java', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_forOf_with_java(self):
        js_code = Unittest('for (elem of arr) {\n\t5\n}', 'js')
        py_code = Unittest('for elem in arr:\n\t5', 'py')
        java_code = Unittest('for (GenericType elem : arr) {\n\t5;\n}', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])


if __name__ == '__main__':
    unittest2.main()
