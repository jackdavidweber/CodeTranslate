import unittest2
import test_matrix


class TestDictionaries(unittest2.TestCase):

    def test_assignment_with_dict(self):
        js_code = 'let d = {1: 2}'
        py_code = 'd = {1: 2}'
        test_matrix.test(self, py_code, js_code)

    def test_print_dictionary(self):
        js_code = 'console.log({"first": true})'
        py_code = 'print({"first": True})'
        test_matrix.test(self, py_code, js_code)

    def test_function_dictionary_argument(self):
        js_code = 'my.function({"4": 1 + 1})'
        py_code = 'my.function({"4": 1 + 1})'
        test_matrix.test(self, py_code, js_code)


if __name__ == '__main__':
    unittest2.main()
