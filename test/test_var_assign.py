import sys

sys.path.append('../cjs_capstone')

import unittest2
import main

class TestVarAssign(unittest2.TestCase):
    def test_string_assign(self):
        self.assertEqual('x = "hi"', main.main('let x = "hi"', 'js', 'py'))
        self.assertEqual('let test = "working"', main.main('test = "working"', 'py', 'js'))
    
    def test_int_assign(self):
        self.assertEqual('num = 109', main.main('const num = 109', 'js', 'py'))
        self.assertEqual('let n = 12', main.main('n = 12', 'py', 'js'))
    
    def test_array_assign(self):
        self.assertEqual('arr = [3, 6]', main.main('let arr = [3, 6]', 'js', 'py'))
        self.assertEqual('let nest = [[1, 9], [2, 8]]', main.main('nest = [[1,9],[2,8]]', 'py', 'js'))
    
    def test_boolean_assign(self):
        self.assertEqual('boo = True', main.main('const boo=true', 'js', 'py'))
        self.assertEqual('let lean = false', main.main('lean = False', 'py', 'js'))
    
    def test_none_assign(self):
        self.assertEqual('no = None', main.main('let no =null', 'js', 'py'))
        self.assertEqual('let help = null', main.main('help = None', 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()