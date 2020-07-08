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
        #TODO since we don't have context it adds the let, do we want to change that?
        self.assertEqual('array[3] = []', main.main('array[3] = []', 'py', 'js')) 
    

if __name__ == '__main__':
    unittest2.main()