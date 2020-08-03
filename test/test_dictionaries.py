import unittest2
import matrix
from Unittest import Unittest


class TestDictionaries(unittest2.TestCase):

    def test_assignment_with_dict(self):
        js_code = Unittest('let d = {1: 2}', "js")
        py_code = Unittest('d = {1: 2}', "py")
        matrix.matrix(self, [py_code, js_code])

    def test_print_dictionary(self):
        js_code = Unittest('console.log({"first": true})', "js")
        py_code = Unittest('print({"first": True})', "py")
        matrix.matrix(self, [py_code, js_code])

    def test_function_dictionary_argument(self):
        js_code = Unittest('my.function({"4": 1 + 1})', "js")
        py_code = Unittest('my.function({"4": 1 + 1})', "py")
        matrix.matrix(self, [py_code, js_code])


if __name__ == '__main__':
    unittest2.main()
