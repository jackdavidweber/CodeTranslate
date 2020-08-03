import unittest2
import matrix
from Unittest import Unittest


class TestCustomFunctions(unittest2.TestCase):

    def test_no_args_no_object(self):
        js_code = Unittest('myFunction()', 'js')
        py_code = Unittest('myFunction()', 'py')
        bash_code = Unittest('myFunction ', 'bash', is_input=False)
        java_code = Unittest('myFunction();', 'java')
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_one_arg_no_object(self):
        js_code = Unittest('run("fast")', 'js')
        py_code = Unittest('run("fast")', 'py')
        bash_code = Unittest('run "fast"', 'bash', is_input=False)
        java_code = Unittest('run("fast");', 'java')
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_two_args(self):
        js_code = Unittest('greeting("hi", 1)', 'js')
        py_code = Unittest('greeting("hi", 1)', 'py')
        bash_code = Unittest('greeting "hi" 1', 'bash', is_input=False)
        java_code = Unittest('greeting("hi", 1);', 'java')
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])

    def test_object(self):
        js_code = Unittest('my.function()', 'js')
        py_code = Unittest('my.function()', 'py')
        java_code = Unittest('my.function();', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_object_attribute(self):
        js_code = Unittest('car.honda.drive(1, 2)', 'js')
        py_code = Unittest('car.honda.drive(1, 2)', 'py')
        java_code = Unittest('car.honda.drive(1, 2);', 'java')
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_arg_varaible(self):
        js_code = Unittest('test(file)', 'js')
        py_code = Unittest('test(file)', 'py')
        java_code = Unittest('test(file);', 'java', is_input=False)
        bash_code = Unittest('test "$file"', 'bash', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code, bash_code])


if __name__ == '__main__':
    unittest2.main()
