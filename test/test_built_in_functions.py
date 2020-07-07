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
    

if __name__ == '__main__':
    unittest2.main()