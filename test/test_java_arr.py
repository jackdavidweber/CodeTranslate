import unittest2
import main


class TestJavaArr(unittest2.TestCase):
    
    def test_arr_to_code(self):
        self.assertEqual('{1, 2};', main.main('[1, 2]', 'py', 'java'))

    def test_log_arr_to_code(self):
        py_input = 'print([1, 2, 3])'
        expected = 'System.out.println(Arrays.toString(new int[] {1, 2, 3}));'
        self.assertEqual(expected, main.main(py_input, 'py', 'java'))
    

if __name__ == '__main__':
    unittest2.main()
