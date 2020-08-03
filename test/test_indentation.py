import unittest2
import matrix
from Unittest import Unittest


class TestIndentation(unittest2.TestCase):

    def test_indent_if(self):
        py_code = Unittest('if (x == True):\n\tif (y == True):\n\t\tprint("y and x are true")', 'py')
        js_code = Unittest('if (x == true) {\n\tif (y == true) {\n\t\tconsole.log("y and x are true")\n\t}\n}', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_indent_for_of(self):
        py_code = Unittest('for j in [1, 2]:\n\tfor k in [3, 4]:\n\t\tj\n\t\tk', 'py')
        js_code = Unittest('for (j of [1, 2]) {\n\tfor (k of [3, 4]) {\n\t\tj\n\t\tk\n\t}\n}', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_indent_for_range(self):
        py_code = Unittest('for j in range (0, 10, 1):\n\tfor k in range (20, 30, 1):\n\t\tj\n\t\tk', 'py')
        js_code = Unittest('for (let j = 0; j < 10; j += 1) {\n\tfor (let k = 20; k < 30; k += 1) {\n\t\tj\n\t\tk\n\t}\n}', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_indent_while(self):
        py_code = Unittest('while (1):\n\twhile (2):\n\t\t3', 'py')
        js_code = Unittest('while (1) {\n\twhile (2) {\n\t\t3\n\t}\n}', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_indent_func_and_if(self):
        py_code = Unittest('def test():\n\tif (1):\n\t\t2', 'py')
        js_code = Unittest('function test() {\n\tif (1) {\n\t\t2\n\t}\n}', 'js')
        matrix.matrix(self, [py_code, js_code])

    def test_indent_func_if_while_for(self):
        py_code = Unittest('def test():\n\tif (1):\n\t\twhile (2):\n\t\t\tfor j in [3, 4]:\n\t\t\t\t5', 'py')
        js_code = Unittest('function test() {\n\tif (1) {\n\t\twhile (2) {\n\t\t\tfor (j of [3, 4]) {\n\t\t\t\t5\n\t\t\t}\n\t\t}\n\t}\n}', 'js')
        matrix.matrix(self, [py_code, js_code])


if __name__ == '__main__':
    unittest2.main()
