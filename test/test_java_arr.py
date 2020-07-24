import unittest2
import translate


class TestJavaArr(unittest2.TestCase):

    def test_arr_to_code(self):
        self.assertEqual('{1, 2};', translate.translate('[1, 2]', 'py', 'java'))

    def test_log_arr_to_code(self):
        py_input = 'print([1, 2, 3])'
        expected = 'System.out.println(Arrays.toString(new int[] {1, 2, 3}));'
        self.assertEqual(expected, translate.translate(py_input, 'py', 'java'))


if __name__ == '__main__':
    unittest2.main()
