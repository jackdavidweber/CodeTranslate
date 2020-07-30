import unittest2
import translate
import test_matrix


class TestBuiltInFunctions(unittest2.TestCase):

    def test_append_statement(self):
        py_code = 'arr.append(x)'
        js_code = 'arr.push(x)'
        test_matrix.test(self, py_code, js_code)

    def test_pop_statement(self):
        py_code = 'arr.pop(1)'
        js_code = 'arr.pop(1)'
        test_matrix.test(self, py_code, js_code)

    def test_array_look_up(self):
        py_code = 'arr[x]'
        js_code = 'arr[x]'
        test_matrix.test(self, py_code, js_code)

    def test_array_assign(self):
        py_code = 'arr[x] = 6'
        js_code = 'arr[x] = 6'
        test_matrix.test(self, py_code, js_code)

    def test_sort(self):
        py_code = 'myArr.sort()'
        js_code = 'myArr.sort()'
        test_matrix.test(self, py_code, js_code)

    def test_extend(self):
        py_code = 'arr1.extend(arr2)'
        js_code = 'arr1.concat(arr2)'
        test_matrix.test(self, py_code, js_code)

    def test_reverse(self):
        py_code = 'arr1.reverse()'
        js_code = 'arr1.reverse()'
        test_matrix.test(self, py_code, js_code)

    def test_string_search(self):
        py_code = 'str.find()'
        js_code = 'str.search()'
        test_matrix.test(self, py_code, js_code)

    def test_string_split(self):
        py_code = 'str.split()'
        js_code = 'str.split()'
        test_matrix.test(self, py_code, js_code)

    def test_string_lower(self):
        py_code = 'str.lower()'
        js_code = 'str.toLowerCase()'
        test_matrix.test(self, py_code, js_code)

    def test_string_upper(self):
        py_code = 'str.upper()'
        js_code = 'str.toUpperCase()'
        test_matrix.test(self, py_code, js_code)

    def test_string_index(self):
        py_code = 'str.index()'
        js_code = 'str.indexOf()'
        test_matrix.test(self, py_code, js_code)

    def test_string_join(self):
        py_code = 'str.join()'
        js_code = 'str.join()'
        test_matrix.test(self, py_code, js_code)

    def test_dictionary_set(self):
        py_code = 'dict.update(key, value)'
        js_code = 'dict.set(key, value)'
        test_matrix.test(self, py_code, js_code)

    def test_dictionary_keys(self):
        py_code = 'dict.keys()'
        js_code = 'dict.keys()'
        test_matrix.test(self, py_code, js_code)

    def test_dictionary_values(self):
        py_code = 'dict.values()'
        js_code = 'dict.values()'
        test_matrix.test(self, py_code, js_code)

    def test_clear(self):
        py_code = 'clear()'
        js_code = 'clear()'
        test_matrix.test(self, py_code, js_code)


if __name__ == '__main__':
    unittest2.main()
