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
    
    def test_java_simple(self):
        java_input = 'public void test() {}'
        java_output = 'public unknown unknown test() {\n\t\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))

    def test_java_simple_arg(self):
        java_input = 'public void test(int x) {1;}'
        java_output = 'public unknown unknown test(customType x) {\n\t1\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))
    
    def test_java_multiple_args(self):
        java_input = 'public void test(int x, String s, int y) {1;}'
        java_output = 'public unknown unknown test(customType x, customType s, customType y) {\n\t1\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))

    def test_java_multiline(self):
        java_input = 'public void test(int x) {1;\n System.out.println(2);}'
        java_output = 'public unknown unknown test(customType x) {\n\t1\n\tSystem.out.println(2)\n}'
        self.assertEqual(java_output, main.main(java_input, 'java', 'java'))

if __name__ == '__main__':
    unittest2.main()