import unittest2
import matrix


class TestBuiltInFunctions(unittest2.TestCase):

    def test_append_statement(self):
        py_code = 'arr.append(x)'
        js_code = 'arr.push(x)'
        matrix.test(self, py_code, js_code)

    def test_pop_statement(self):
        py_code = 'arr.pop(1)'
        js_code = 'arr.pop(1)'
        matrix.test(self, py_code, js_code)

    def test_array_look_up(self):
        py_code = 'arr[x]'
        js_code = 'arr[x]'
        matrix.test(self, py_code, js_code)

    def test_array_assign(self):
        py_code = 'arr[x] = 6'
        js_code = 'arr[x] = 6'
        matrix.test(self, py_code, js_code)

    def test_sort(self):
        py_code = 'myArr.sort()'
        js_code = 'myArr.sort()'
        matrix.test(self, py_code, js_code)

    def test_extend(self):
        py_code = 'arr1.extend(arr2)'
        js_code = 'arr1.concat(arr2)'
        matrix.test(self, py_code, js_code)

    def test_reverse(self):
        py_code = 'arr1.reverse()'
        js_code = 'arr1.reverse()'
        matrix.test(self, py_code, js_code)

    def test_string_search(self):
        py_code = 'str.find()'
        js_code = 'str.search()'
        matrix.test(self, py_code, js_code)

    def test_string_split(self):
        py_code = 'str.split()'
        js_code = 'str.split()'
        matrix.test(self, py_code, js_code)

    def test_string_lower(self):
        py_code = 'str.lower()'
        js_code = 'str.toLowerCase()'
        matrix.test(self, py_code, js_code)

    def test_string_upper(self):
        py_code = 'str.upper()'
        js_code = 'str.toUpperCase()'
        matrix.test(self, py_code, js_code)

    def test_string_index(self):
        py_code = 'str.index()'
        js_code = 'str.indexOf()'
        matrix.test(self, py_code, js_code)

    def test_string_join(self):
        py_code = 'str.join()'
        js_code = 'str.join()'
        matrix.test(self, py_code, js_code)

    def test_dictionary_set(self):
        py_code = 'dict.update(key, value)'
        js_code = 'dict.set(key, value)'
        matrix.test(self, py_code, js_code)

    def test_dictionary_keys(self):
        py_code = 'dict.keys()'
        js_code = 'dict.keys()'
        matrix.test(self, py_code, js_code)

    def test_dictionary_values(self):
        py_code = 'dict.values()'
        js_code = 'dict.values()'
        matrix.test(self, py_code, js_code)

    def test_clear(self):
        py_code = 'clear()'
        js_code = 'clear()'
        matrix.test(self, py_code, js_code)


if __name__ == '__main__':
    unittest2.main()
