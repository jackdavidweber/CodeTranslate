import unittest2
import main

class TestCustomFunctions(unittest2.TestCase):
    def test_no_args_no_object(self):
        self.assertEqual('myFunction()', main.main('myFunction()', 'py', 'js'))
        self.assertEqual('drive()', main.main('drive()', 'js', 'py'))
    
    def test_one_arg_no_object(self):
        self.assertEqual('run("fast")', main.main('run("fast")', 'py', 'js'))
        self.assertEqual('sprint("slow")', main.main('sprint("slow")', 'js', 'py'))
    
    def test_object(self):
        self.assertEqual('my.function()', main.main('my.function()', 'js', 'py'))
        self.assertEqual('hello.world()', main.main('hello.world()', 'py', 'js'))
    
    def test_object_attribute(self):
        self.assertEqual('car.honda.drive(1, 3)', main.main('car.honda.drive(1,3)', 'js', 'py'))
        self.assertEqual('car.ford.park(null)', main.main('car.ford.park(None)', 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()