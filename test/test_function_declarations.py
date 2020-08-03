import unittest2
import translate
import matrix
from Unittest import Unittest


class TestFunctionDeclarations(unittest2.TestCase):

    def test_function_no_args(self):
        js_code = Unittest('function test() {\n\t2\n}', 'js')
        py_code = Unittest('def test():\n\t2', 'py')
        java_code = Unittest('public void test() {\n\t2;\n}', 'java', is_output=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_function_one_arg(self):
        js_code = Unittest('function test(x) {\n\tconsole.log(x)\n}', 'js')
        py_code = Unittest('def test(x):\n\tprint(x)', 'py')
        java_code = Unittest('class Test {\n\tpublic unknown unknown test(CustomType x) {\n\t\tSystem.out.println(x);\n\t}\n}', 'java', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_function_multiple_args(self):
        js_code = Unittest('function test(x, y, z) {\n\tconsole.log(x + y + z)\n}', 'js')
        py_code = Unittest('def test(x, y, z):\n\tprint(x + y + z)', 'py')
        java_code = Unittest('class Test {\n\tpublic unknown unknown test(CustomType x, CustomType y, CustomType z) {\n\t\tSystem.out.println(x + y + z);\n\t}\n}', 'java', is_input=False)
        matrix.matrix(self, [py_code, js_code, java_code])

    def test_function_multi_line_body(self):
        js_code = Unittest('function test(x, y, z) {\n\tconsole.log(x)\n\tconsole.log(y)\n\tconsole.log(z)\n}', 'js')
        py_code = Unittest('def test(x, y, z):\n\tprint(x)\n\tprint(y)\n\tprint(z)', 'py')
        matrix.matrix(self, [py_code, js_code])

    def test_simple_return(self):
        js_code = Unittest('function test() {\n\treturn 1\n}', 'js')
        py_code = Unittest('def test():\n\treturn 1', 'py')
        matrix.matrix(self, [py_code, js_code])

    def test_complicated_function(self):
        js_code = Unittest('function test(x, y, z) {\n\tconsole.log(x)\n\tconsole.log(y)\n\tconsole.log(z)\n\treturn x + y + z\n}', 'js')
        py_code = Unittest('def test(x, y, z):\n\tprint(x)\n\tprint(y)\n\tprint(z)\n\treturn x + y + z', 'py')
        matrix.matrix(self, [py_code, js_code])

    def test_default_vals(self):
        js_code = Unittest('function test(x = 1) {\n\tconsole.log(x)\n}', 'js')
        py_code = Unittest('def test(x = 1):\n\tprint(x)', 'py')
        matrix.matrix(self, [py_code, js_code])

    def test_multiple_default_vals(self):
        js_code = Unittest('function test(x, y = 2, z = 4, a = 1) {\n\treturn y\n}', 'js')
        py_code = Unittest('def test(x, y = 2, z = 4, a = 1):\n\treturn y', 'py')
        matrix.matrix(self, [py_code, js_code])

    def test_java_func_no_arg_no_body(self):
        java_input = Unittest('public void test() {}', 'java', is_output=False)
        java_output = Unittest('class Test {\n\tpublic unknown unknown test() {\n\t\t\n\t}\n}', 'java', is_input=False)
        matrix.matrix(self, [java_input, java_output])

    def test_java_func_arg(self):
        java_input = Unittest('public void test(int x) {1;}', 'java', is_output=False)
        java_output = Unittest('class Test {\n\tpublic unknown unknown test(CustomType x) {\n\t\t1;\n\t}\n}', 'java', is_input=False)
        matrix.matrix(self, [java_input, java_output])

    def test_java_multiple_args(self):
        java_input = Unittest('public void test(int x, String s, int y) {1;}', 'java', is_output=False)
        java_output = Unittest('class Test {\n\tpublic unknown unknown test(CustomType x, CustomType s, CustomType y) {\n\t\t1;\n\t}\n}', 'java', is_input=False)
        matrix.matrix(self, [java_input, java_output])

    def test_java_multiline(self):
        java_input = Unittest('public void test(int x) {1;\n System.out.println(2);}', 'java', is_output=False)
        java_output = Unittest('class Test {\n\tpublic unknown unknown test(CustomType x) {\n\t\t1;\n\t\tSystem.out.println(2);\n\t}\n}', 'java', is_input=False)
        matrix.matrix(self, [java_input, java_output])

    def test_java_main_function(self):
        js_input = Unittest('function s() {2}\nconsole.log(1)', 'js', is_output=False)
        java_output = Unittest('class Test {\n\tpublic unknown unknown s() {\n\t\t2;\n\t}\n\t\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println(1);\n\t}\n}', 'java', is_input=False)
        matrix.matrix(self, [js_input, java_output])

    def test_blank_arrow_functions(self):
        #note python won't compile in this case
        js_input = Unittest('() => {\n\t\n}', 'js', is_output=False)
        py_output = Unittest('lambda:', 'py', is_input=False)
        matrix.matrix(self, [js_input, py_output])

    def test_basic_arrow_functions(self):
        js_output = Unittest( '() => {\n\t1\n}', 'js', is_input=False)
        py_input = Unittest('lambda: 1', 'py', is_output=False)
        matrix.matrix(self, [js_output, py_input])

    def test_basic_arrow_anon_functions(self):
        js_code = Unittest('let a = () => {\n\t1\n}', 'js')
        js_input = Unittest('let a = function() {\n\t1\n}', 'js', is_output=False)
        py_code = Unittest('a = lambda: 1', 'py')
        matrix.matrix(self, [js_code, js_input, py_code])

    def test_arrow_anon_functions_args(self):
        js_code = Unittest('let a = (x) => {\n\t1\n}', 'js')
        js_input = Unittest('let a = function(x) {\n\t1\n}', 'js', is_output=False)
        py_code = Unittest('a = lambda x: 1', 'py')
        matrix.matrix(self, [js_code, js_input, py_code])

    def test_arrow_anon_functions_complex(self):
        js_code = Unittest('let a = (x, y, z) => {\n\t1\n}', 'js')
        js_input = Unittest('let a = function(x, y, z) {\n\t1\n}', 'js', is_output=False)
        py_code = Unittest('a = lambda x, y, z: 1', 'py')
        matrix.matrix(self, [js_code, js_input, py_code])


if __name__ == '__main__':
    unittest2.main()
