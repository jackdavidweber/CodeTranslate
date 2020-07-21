import unittest2
import main


class TestCustomFunctions(unittest2.TestCase):

    def test_no_args_no_object(self):
        self.assertEqual('myFunction()', main.main('myFunction()', 'py', 'js')['translation']['output_code'])
        self.assertEqual('drive()', main.main('drive()', 'js', 'py')['translation']['output_code'])
        self.assertEqual('test ', main.main('test()', 'js', 'bash')['translation']['output_code'])

    def test_one_arg_no_object(self):
        self.assertEqual('run("fast")', main.main('run("fast")', 'py', 'js')['translation']['output_code'])
        self.assertEqual('sprint("slow")',
                         main.main('sprint("slow")', 'js', 'py')['translation']['output_code'])
        self.assertEqual('hello "joe" 1',
                         main.main('hello("joe", 1)', 'js', 'bash')['translation']['output_code'])

    def test_object(self):
        self.assertEqual('my.function()', main.main('my.function()', 'js',
                                                    'py'))
        self.assertEqual('hello.world()', main.main('hello.world()', 'py',
                                                    'js'))

    def test_object_attribute(self):
        self.assertEqual('car.honda.drive(1, 3)',
                         main.main('car.honda.drive(1,3)', 'js', 'py')['translation']['output_code'])
        self.assertEqual('car.ford.park(null)',
                         main.main('car.ford.park(None)', 'py', 'js')['translation']['output_code'])

    def test_arg_varaible(self):
        self.assertEqual('test "$file"', main.main('test(file)', 'js', 'bash')['translation']['output_code'])
        self.assertEqual('test "$one" "$two"',
                         main.main('test(one, two)', 'py', 'bash')['translation']['output_code'])


if __name__ == '__main__':
    unittest2.main()
