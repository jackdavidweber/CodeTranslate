import unittest2
import matrix
from Unittest import Unittest


class TestBuiltInFunctions(unittest2.TestCase):

    def test_append_statement(self):
        py_code = Unittest('arr.append(x)', 'py')
        js_code = Unittest('arr.push(x)', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_pop_statement(self):
        py_code = Unittest('arr.pop(1)', 'py')
        js_code = Unittest('arr.pop(1)', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_array_look_up(self):
        py_code = Unittest('arr[x]', 'py')
        js_code = Unittest('arr[x]', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_array_assign(self):
        py_code = Unittest('arr[x] = 6', 'py')
        js_code = Unittest('arr[x] = 6', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_sort(self):
        py_code = Unittest('myArr.sort()', 'py')
        js_code = Unittest('myArr.sort()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_extend(self):
        py_code = Unittest('arr1.extend(arr2)', 'py')
        js_code = Unittest('arr1.concat(arr2)', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_reverse(self):
        py_code = Unittest('arr.reverse()', 'py')
        js_code = Unittest('arr.reverse()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_string_search(self):
        py_code = Unittest('str.find(x)', 'py')
        js_code = Unittest('str.search(x)', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_string_split(self):
        py_code = Unittest('str.split()', 'py')
        js_code = Unittest('str.split()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_string_lower(self):
        py_code = Unittest('str.lower()', 'py')
        js_code = Unittest('str.toLowerCase()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_string_upper(self):
        py_code = Unittest('str.upper()', 'py')
        js_code = Unittest('str.toUpperCase()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_string_index(self):
        py_code = Unittest('str.index(x)', 'py')
        js_code = Unittest('str.indexOf(x)', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_string_join(self):
        py_code = Unittest('str.join()', 'py')
        js_code = Unittest('str.join()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_dictionary_set(self):
        py_code = Unittest('dict.update(key, value)', 'py')
        js_code = Unittest('dict.set(key, value)', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_dictionary_keys(self):
        py_code = Unittest('dict.keys()', 'py')
        js_code = Unittest('dict.keys()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_dictionary_values(self):
        py_code = Unittest('dict.values()', 'py')
        js_code = Unittest('dict.values()', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_clear(self):
        py_code = Unittest('clear()', 'py')
        js_code = Unittest('clear()', 'js')
        matrix.matrix(self, [py_code, js_code])


if __name__ == '__main__':
    unittest2.main()
