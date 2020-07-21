import unittest2
import main


class TestBuiltInFunctions(unittest2.TestCase):

    def test_append_statement(self):
        self.assertEqual('arr.push(x)', main.main('arr.append(x)', 'py', 'js')['translation']['output_code'])
        self.assertEqual('arr.append(x)', main.main('arr.push(x)', 'js', 'py')['translation']['output_code'])

    def test_pop_statement(self):
        self.assertEqual('arr.pop(1)', main.main('arr.pop(1)', 'py', 'js')['translation']['output_code'])
        self.assertEqual('mine.pop(True)',
                         main.main('mine.pop(true)', 'js', 'py')['translation']['output_code'])

    def test_array_look_up(self):
        self.assertEqual('arr[x]', main.main('arr[x]', 'js', 'py')['translation']['output_code'])
        self.assertEqual('array[3]', main.main('array[3]', 'py', 'js')['translation']['output_code'])

    def test_array_assign(self):
        self.assertEqual('arr[x] = 6', main.main('arr[x] = 6', 'js', 'py')['translation']['output_code'])
        self.assertEqual('array[3] = []', main.main('array[3] = []', 'py',
                                                    'js'))

    def test_sort(self):
        self.assertEqual('myArr.sort()', main.main('myArr.sort()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('rr.sort()', main.main('rr.sort()', 'py', 'js')['translation']['output_code'])

    def test_extend(self):
        self.assertEqual('arr1.extend(arr2)',
                         main.main('arr1.concat(arr2)', 'js', 'py')['translation']['output_code'])
        self.assertEqual('arr1.concat(arr2)',
                         main.main('arr1.extend(arr2)', 'py', 'js')['translation']['output_code'])

    def test_reverse(self):
        self.assertEqual('arr1.reverse()',
                         main.main('arr1.reverse()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('arr1.reverse()',
                         main.main('arr1.reverse()', 'py', 'js')['translation']['output_code'])

    def test_string_search(self):
        self.assertEqual('str.find()', main.main('str.search()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('str.search()', main.main('str.find()', 'py', 'js')['translation']['output_code'])

    def test_string_split(self):
        self.assertEqual('str.split()', main.main('str.split()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('str.split()', main.main('str.split()', 'py', 'js')['translation']['output_code'])

    def test_string_lower(self):
        self.assertEqual('str.lower()',
                         main.main('str.toLowerCase()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('str.toLowerCase()',
                         main.main('str.lower()', 'py', 'js')['translation']['output_code'])

    def test_string_upper(self):
        self.assertEqual('str.upper()',
                         main.main('str.toUpperCase()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('str.toUpperCase()',
                         main.main('str.upper()', 'py', 'js')['translation']['output_code'])

    def test_string_index(self):
        self.assertEqual('str.index()', main.main('str.indexOf()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('str.indexOf()', main.main('str.index()', 'py', 'js')['translation']['output_code'])

    def test_string_join(self):
        self.assertEqual('str.join()', main.main('str.join()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('str.join()', main.main('str.join()', 'py', 'js')['translation']['output_code'])

    def test_dictionary_set(self):
        self.assertEqual('dict.update(key, value)',
                         main.main('dict.set(key,value)', 'js', 'py')['translation']['output_code'])
        self.assertEqual('dict.set(key, value)',
                         main.main('dict.update(key, value)', 'py', 'js')['translation']['output_code'])

    def test_dictionary_keys(self):
        self.assertEqual('dict.keys()', main.main('dict.keys()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('dict.keys()', main.main('dict.keys()', 'py', 'js')['translation']['output_code'])

    def test_dictionary_keys(self):
        self.assertEqual('dict.values()', main.main('dict.values()', 'js',
                                                    'py'))
        self.assertEqual('dict.values()', main.main('dict.values()', 'py',
                                                    'js'))

    def test_clear(self):
        self.assertEqual('clear()', main.main('clear()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('clear()', main.main('clear()', 'py', 'js')['translation']['output_code'])


if __name__ == '__main__':
    unittest2.main()
