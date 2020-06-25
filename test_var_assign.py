import unittest2
import main

class TestLogStatement(unittest2.TestCase):
    def test_string_assign(self):
        self.assertEqual('x = "hi"', main.main('let x = "hi"', 'js', 'py'))
        self.assertEqual('const test = "working"', main.main('test = "working"', 'py', 'js'))
    
    def test_int_assign(self):
        self.assertEqual('num = 109', main.main('const num = 109', 'js', 'py'))
        self.assertEqual('const n = 12', main.main('n = 12', 'py', 'js'))
    
    def test_array_assign(self):
        self.assertEqual('arr = [3, 6]', main.main('let arr = [3, 6]', 'js', 'py'))
        self.assertEqual('const nest = [[1, 9], [2, 8]]', main.main('nest = [[1,9],[2,8]]', 'py', 'js'))
    
    def test_boolean_assign(self):
        self.assertEqual('boo = True', main.main('const boo=True', 'js', 'py'))
        self.assertEqual('const lean = false', main.main('lean = False', 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()