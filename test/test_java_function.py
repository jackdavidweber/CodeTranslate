import unittest2
import translate


class TestJavaFunctionCalls(unittest2.TestCase):


    def test_function_on_object(self):
        code = 'car.drive("hi");'
        self.assertEqual('car.drive("hi");',
                         translate.translate(code, 'java', 'java'))

    def test_function_multiple_objects(self):
        code = 'nice.car.drive();'
        self.assertEqual('nice.car.drive();',
                         translate.translate(code, 'java', 'java'))

    def test_complex_function(self):
        code = 'really.fancy.and.nice.car.drive();'
        self.assertEqual('really.fancy.and.nice.car.drive();',
                         translate.translate(code, 'java', 'java'))


if __name__ == '__main__':
    unittest2.main()
