import unittest2
import translate
import test_matrix


class TestLogStatement(unittest2.TestCase):

    def test_no_args(self):
        py_code = 'print()'
        js_code = 'console.log()'
        bash_code = 'echo '
        java_code = 'System.out.println();'
        test_matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_one_arg(self):
        py_code = 'print("hello")'
        js_code = 'console.log("hello")'
        bash_code = 'echo "hello"'
        java_code = 'System.out.println("hello");'
        test_matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_arrays(self):
        py_code = 'print([[1, 3], [3, 4]])'
        js_code = 'console.log([[1, 3], [3, 4]])'
        test_matrix.test(self, py_code, js_code)

    def test_boolean(self):
        py_code = 'print(True)'
        js_code = 'console.log(true)'
        java_code = 'System.out.println(true);'
        test_matrix.test(self, py_code, js_code, java_code)

    def test_none(self):
        py_code = 'print(None)'
        js_code = 'console.log(null)'
        test_matrix.test(self, py_code, js_code)
    
    def test_log_arr_to_code(self):
        py_input = 'print([1, 2, 3])'
        expected = 'System.out.println(Arrays.toString(new int[] {1, 2, 3}));'
        self.assertEqual(expected, translate.translate(py_input, 'py', 'java'))


if __name__ == '__main__':
    unittest2.main()
