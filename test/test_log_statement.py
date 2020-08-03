import unittest2
import matrix
from Unittest import Unittest


class TestLogStatement(unittest2.TestCase):

    def test_no_args(self):
        py_code = Unittest('print()', 'py')
        js_code = Unittest('console.log()', 'js')
        java_code = Unittest('System.out.println();', 'java')
        bash_code = Unittest('echo ', 'bash', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_one_arg(self):
        py_code = Unittest('print("hello")', 'py')
        js_code = Unittest('console.log("hello")', 'js')
        java_code = Unittest('System.out.println("hello");', 'java')
        bash_code = Unittest('echo "hello"', 'bash', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_arrays(self):
        py_code = Unittest('print([[1, 3], [3, 4]])', 'py')
        js_code = Unittest('console.log([[1, 3], [3, 4]])', 'js')
        java_code = Unittest(
            'System.out.println(Arrays.toString(new int[][] {{1, 3}, {3, 4}}));',
            'java',
            is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_boolean(self):
        py_code = Unittest('print(True)', 'py')
        js_code = Unittest('console.log(true)', 'js')
        java_code = Unittest('System.out.println(true);', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_none(self):
        py_code = Unittest('print(None)', 'py')
        js_code = Unittest('console.log(null)', 'js')
        java_code = Unittest('System.out.println(null);',
                             'java',
                             is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_log_arr_to_code(self):
        py_code = Unittest('print([1, 2, 3])', "py")
        java_output = Unittest(
            'System.out.println(Arrays.toString(new int[] {1, 2, 3}));',
            'java',
            is_input=False)
        matrix.matrix(self, [py_code, java_output])


if __name__ == '__main__':
    unittest2.main()
