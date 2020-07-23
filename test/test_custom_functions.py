import unittest2
import translate


class TestCustomFunctions(unittest2.TestCase):

    def test_no_args_no_object(self):
        self.assertEqual('myFunction()', translate.translate('myFunction()', 'py', 'js'))
        self.assertEqual('drive()', translate.translate('drive()', 'js', 'py'))
        self.assertEqual('test ', translate.translate('test()', 'js', 'bash'))

    def test_one_arg_no_object(self):
        self.assertEqual('run("fast")', translate.translate('run("fast")', 'py', 'js'))
        self.assertEqual('sprint("slow")',
                         translate.translate('sprint("slow")', 'js', 'py'))
        self.assertEqual('hello "joe" 1',
                         translate.translate('hello("joe", 1)', 'js', 'bash'))

    def test_object(self):
        self.assertEqual('my.function()', translate.translate('my.function()', 'js',
                                                    'py'))
        self.assertEqual('hello.world()', translate.translate('hello.world()', 'py',
                                                    'js'))

    def test_object_attribute(self):
        self.assertEqual('car.honda.drive(1, 3)',
                         translate.translate('car.honda.drive(1,3)', 'js', 'py'))
        self.assertEqual('car.ford.park(null)',
                         translate.translate('car.ford.park(None)', 'py', 'js'))

    def test_arg_varaible(self):
        self.assertEqual('test "$file"', translate.translate('test(file)', 'js', 'bash'))
        self.assertEqual('test "$one" "$two"',
                         translate.translate('test(one, two)', 'py', 'bash'))


if __name__ == '__main__':
    unittest2.main()
