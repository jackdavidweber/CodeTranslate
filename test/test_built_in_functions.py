import unittest2
import translate


class TestBuiltInFunctions(unittest2.TestCase):

    def test_append_statement(self):
        self.assertEqual('arr.push(x)',
                         translate.translate('arr.append(x)', 'py', 'js'))
        self.assertEqual('arr.append(x)',
                         translate.translate('arr.push(x)', 'js', 'py'))

    def test_pop_statement(self):
        self.assertEqual('arr.pop(1)',
                         translate.translate('arr.pop(1)', 'py', 'js'))
        self.assertEqual('mine.pop(True)',
                         translate.translate('mine.pop(true)', 'js', 'py'))

    def test_array_look_up(self):
        self.assertEqual('arr[x]', translate.translate('arr[x]', 'js', 'py'))
        self.assertEqual('array[3]',
                         translate.translate('array[3]', 'py', 'js'))

    def test_array_assign(self):
        self.assertEqual('arr[x] = 6',
                         translate.translate('arr[x] = 6', 'js', 'py'))
        self.assertEqual('array[3] = []',
                         translate.translate('array[3] = []', 'py', 'js'))

    def test_sort(self):
        self.assertEqual('myArr.sort()',
                         translate.translate('myArr.sort()', 'js', 'py'))
        self.assertEqual('rr.sort()',
                         translate.translate('rr.sort()', 'py', 'js'))

    def test_extend(self):
        self.assertEqual('arr1.extend(arr2)',
                         translate.translate('arr1.concat(arr2)', 'js', 'py'))
        self.assertEqual('arr1.concat(arr2)',
                         translate.translate('arr1.extend(arr2)', 'py', 'js'))

    def test_reverse(self):
        self.assertEqual('arr1.reverse()',
                         translate.translate('arr1.reverse()', 'js', 'py'))
        self.assertEqual('arr1.reverse()',
                         translate.translate('arr1.reverse()', 'py', 'js'))

    def test_string_search(self):
        self.assertEqual('str.find()',
                         translate.translate('str.search()', 'js', 'py'))
        self.assertEqual('str.search()',
                         translate.translate('str.find()', 'py', 'js'))

    def test_string_split(self):
        self.assertEqual('str.split()',
                         translate.translate('str.split()', 'js', 'py'))
        self.assertEqual('str.split()',
                         translate.translate('str.split()', 'py', 'js'))

    def test_string_lower(self):
        self.assertEqual('str.lower()',
                         translate.translate('str.toLowerCase()', 'js', 'py'))
        self.assertEqual('str.toLowerCase()',
                         translate.translate('str.lower()', 'py', 'js'))

    def test_string_upper(self):
        self.assertEqual('str.upper()',
                         translate.translate('str.toUpperCase()', 'js', 'py'))
        self.assertEqual('str.toUpperCase()',
                         translate.translate('str.upper()', 'py', 'js'))

    def test_string_index(self):
        self.assertEqual('str.index()',
                         translate.translate('str.indexOf()', 'js', 'py'))
        self.assertEqual('str.indexOf()',
                         translate.translate('str.index()', 'py', 'js'))

    def test_string_join(self):
        self.assertEqual('str.join()',
                         translate.translate('str.join()', 'js', 'py'))
        self.assertEqual('str.join()',
                         translate.translate('str.join()', 'py', 'js'))

    def test_dictionary_set(self):
        self.assertEqual('dict.update(key, value)',
                         translate.translate('dict.set(key,value)', 'js', 'py'))
        self.assertEqual(
            'dict.set(key, value)',
            translate.translate('dict.update(key, value)', 'py', 'js'))

    def test_dictionary_keys(self):
        self.assertEqual('dict.keys()',
                         translate.translate('dict.keys()', 'js', 'py'))
        self.assertEqual('dict.keys()',
                         translate.translate('dict.keys()', 'py', 'js'))

    def test_dictionary_keys(self):
        self.assertEqual('dict.values()',
                         translate.translate('dict.values()', 'js', 'py'))
        self.assertEqual('dict.values()',
                         translate.translate('dict.values()', 'py', 'js'))

    def test_clear(self):
        self.assertEqual('clear()', translate.translate('clear()', 'js', 'py'))
        self.assertEqual('clear()', translate.translate('clear()', 'py', 'js'))


if __name__ == '__main__':
    unittest2.main()
