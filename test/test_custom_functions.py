import unittest2
import test_matrix


class TestCustomFunctions(unittest2.TestCase):

    def test_no_args_no_object(self):
        py_code = "myFunction()"
        js_code = "myFunction()"
        bash_code = "myFunction "
        java_code = "myFunction();"
        test_matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_one_arg_no_object(self):
        py_code = 'run("fast")'
        js_code = 'run("fast")'
        bash_code = 'run "fast"'
        java_code = 'run("fast");'
        test_matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_two_args(self):
        py_code = 'greeting("hi", 1)'
        js_code = 'greeting("hi", 1)'
        bash_code = 'greeting "hi" 1'
        java_code = 'greeting("hi", 1);'
        test_matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_object(self):
        py_code = 'my.function()'
        js_code = 'my.function()'
        java_code = 'my.function();'
        test_matrix.test(self, py_code, js_code, java_code)

    def test_object_attribute(self):
        py_code = 'car.honda.drive(1, 2)'
        js_code = 'car.honda.drive(1, 2)'
        test_matrix.test(self, py_code, js_code)

    def test_arg_varaible(self):
        py_code = 'test(file)'
        js_code = 'test(file)'
        bash_code = 'test "$file"'
        test_matrix.test(self, py_code, js_code, None, bash_code)


if __name__ == '__main__':
    unittest2.main()
