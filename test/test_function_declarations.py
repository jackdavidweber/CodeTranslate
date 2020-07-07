import sys
sys.path.append('../cjs_capstone')

import unittest2
import main

class TestFunctionDeclarations(unittest2.TestCase):
    def test_function_no_args(self):
        js_code = 'function test() {\n\t2\n}'
        py_code = 'def test():\n\t2'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    
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
    

if __name__ == '__main__':
    unittest2.main()