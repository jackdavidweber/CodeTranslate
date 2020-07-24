import unittest2
import main


class TestFunctionDeclarations(unittest2.TestCase):

    def test_function_no_args(self):
        js_code = 'function test() {\n\t2\n}'
        py_code = 'def test():\n\t2'
        java_code = 'public void test() {\n\t2;\n}'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
        self.assertEqual(js_code, main.main(java_code, 'java', 'js'))
        self.assertEqual(py_code, main.main(java_code, 'java', 'py'))

    def test_function_one_arg(self):
        js_code = 'function test(x) {\n\tconsole.log(x)\n}'
        py_code = 'def test(x):\n\tprint(x)'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_function_multiple_args(self):
        js_code = 'function test(x, y, z) {\n\tconsole.log(x + y + z)\n}'
        py_code = 'def test(x, y, z):\n\tprint(x + y + z)'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_function_multi_line_body(self):
        js_code = 'function test(x, y, z) {\n\tconsole.log(x)\n\tconsole.log(y)'
        js_code += '\n\tconsole.log(z)\n}'
        py_code = 'def test(x, y, z):\n\tprint(x)\n\tprint(y)\n\tprint(z)'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_simple_return(self):
        js_code = 'function test() {\n\treturn 1\n}'
        py_code = 'def test():\n\treturn 1'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_complicated_function(self):
        js_code = 'function test(x, y, z) {\n\tconsole.log(x)\n\tconsole.log(y)'
        js_code += '\n\tconsole.log(z)\n\treturn x + y + z\n}'
        py_code = 'def test(x, y, z):\n\tprint(x)\n\tprint(y)\n\tprint(z)'
        py_code += '\n\treturn x + y + z'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_default_vals(self):
        js_code = 'function test(x = 1) {\n\tconsole.log(x)\n}'
        py_code = 'def test(x = 1):\n\tprint(x)'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_multiple_default_vals(self):
        js_code = 'function test(x, y = 2, z = 4, a = 1) {\n\treturn y\n}'
        py_code = 'def test(x, y = 2, z = 4, a = 1):\n\treturn y'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_java_func_no_arg_no_body(self):
        java_input = 'public void test() {}'
        java_output = 'class Test {\n\tpublic unknown unknown test() {\n\t\t;\n\t}\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))

    def test_java_func_arg(self):
        java_input = 'public void test(int x) {1;}'
        java_output = 'class Test {\n\tpublic unknown unknown test(CustomType x) {\n\t\t1;\n\t}\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))

    def test_java_multiple_args(self):
        java_input = 'public void test(int x, String s, int y) {1;}'
        java_output = 'class Test {\n\tpublic unknown unknown test(CustomType x, CustomType s, CustomType y) {\n\t\t1;\n\t}\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))

    def test_java_multiline(self):
        java_input = 'public void test(int x) {1;\n System.out.println(2);}'
        java_output = 'class Test {\n\tpublic unknown unknown test(CustomType x) {\n\t\t1;\n\t\tSystem.out.println(2);\n\t}\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))

    def test_java_main_function(self):
        js = 'function s() {2}\nconsole.log(1)'
        java = 'class Test {\n\tpublic unknown unknown s() {\n\t\t2;\n\t}\n\t;\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println(1);\n\t}\n}'
        self.assertEqual(java, main.main(js, 'js', 'java'))

    def test_blank_arrow_functions(self):
        #note python won't compile in this case
        js_arrow = '() => {\n\t\n}'
        py_code = 'lambda:'
        self.assertEqual(py_code, main.main(js_arrow, 'js', 'py'))

    def test_basic_arrow_functions(self):
        js_arrow = '() => {\n\t1\n}'
        py_code = 'lambda: 1'
        self.assertEqual(py_code, main.main(js_arrow, 'js', 'py'))
        self.assertEqual(js_arrow, main.main(py_code, 'py', 'js'))

    def test_basic_arrow_anon_functions(self):
        js_arrow = 'let a = () => {\n\t1\n}'
        js_anon = 'let a = function() {\n\t1\n}'
        py_code = 'a = lambda: 1'
        self.assertEqual(py_code, main.main(js_arrow, 'js', 'py'))
        self.assertEqual(py_code, main.main(js_anon, 'js', 'py'))
        self.assertEqual(js_arrow, main.main(py_code, 'py', 'js'))

    def test_arrow_anon_functions_args(self):
        js_arrow = 'let a = (x) => {\n\t1\n}'
        js_anon = 'let a = function(x) {\n\t1\n}'
        py_code = 'a = lambda x: 1'
        self.assertEqual(py_code, main.main(js_arrow, 'js', 'py'))
        self.assertEqual(py_code, main.main(js_anon, 'js', 'py'))
        self.assertEqual(js_arrow, main.main(py_code, 'py', 'js'))

    def test_arrow_anon_functions_complex(self):
        js_arrow = 'let a = (x, y, z) => {\n\t1\n}'
        js_anon = 'let a = function(x, y, z) {\n\t1\n}'
        py_code = 'a = lambda x, y, z: 1'
        self.assertEqual(py_code, main.main(js_arrow, 'js', 'py'))
        self.assertEqual(py_code, main.main(js_anon, 'js', 'py'))
        self.assertEqual(js_arrow, main.main(py_code, 'py', 'js'))


if __name__ == '__main__':
    unittest2.main()
