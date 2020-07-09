import sys
sys.path.append('../cjs_capstone')

import unittest2
import main

class TestBuiltInFunctions(unittest2.TestCase):
    def test_append_statement(self):
        self.assertEqual('arr.push(x)', main.main('arr.append(x)', 'py', 'js'))
        self.assertEqual('arr.append(x)', main.main('arr.push(x)', 'js', 'py'))
    
    def test_pop_statement(self):
        self.assertEqual('arr.pop(1)', main.main('arr.pop(1)', 'py', 'js'))
        self.assertEqual('mine.pop(True)', main.main('mine.pop(true)', 'js', 'py'))
    
    def test_array_look_up(self):
        self.assertEqual('arr[x]', main.main('arr[x]', 'js', 'py'))
        self.assertEqual('array[3]', main.main('array[3]', 'py', 'js'))
    
    def test_array_assign(self):
        self.assertEqual('arr[x] = 6', main.main('arr[x] = 6', 'js', 'py'))
        self.assertEqual('array[3] = []', main.main('array[3] = []', 'py', 'js')) 
    
    def test_sort(self):
        self.assertEqual('myArr.sort()', main.main('myArr.sort()', 'js', 'py'))
        self.assertEqual('rr.sort()', main.main('rr.sort()', 'py', 'js')) 
    
    def test_extend(self):
        self.assertEqual('arr1.extend(arr2)', main.main('arr1.concat(arr2)', 'js', 'py'))
        self.assertEqual('arr1.concat(arr2)', main.main('arr1.extend(arr2)', 'py', 'js'))
    
    def test_reverse(self):
        self.assertEqual('arr1.reverse()', main.main('arr1.reverse()', 'js', 'py'))
        self.assertEqual('arr1.reverse()', main.main('arr1.reverse()', 'py', 'js'))
    
    def test_string_search(self):
        self.assertEqual('str.find()', main.main('str.search()', 'js', 'py'))
        self.assertEqual('str.search()', main.main('str.find()', 'py', 'js'))
    
    def test_string_split(self):
        self.assertEqual('str.split()', main.main('str.split()', 'js', 'py'))
        self.assertEqual('str.split()', main.main('str.split()', 'py', 'js'))
    
    def test_string_lower(self):
        self.assertEqual('str.lower()', main.main('str.toLowerCase()', 'js', 'py'))
        self.assertEqual('str.toLowerCase()', main.main('str.lower()', 'py', 'js'))
    
    def test_string_upper(self):
        self.assertEqual('str.upper()', main.main('str.toUpperCase()', 'js', 'py'))
        self.assertEqual('str.toUpperCase()', main.main('str.upper()', 'py', 'js'))
    
    def test_string_index(self):
        self.assertEqual('str.index()', main.main('str.indexOf()', 'js', 'py'))
        self.assertEqual('str.indexOf()', main.main('str.index()', 'py', 'js'))
    

if __name__ == '__main__':
    unittest2.main()