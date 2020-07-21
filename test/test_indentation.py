import unittest2
import main


class TestIndentation(unittest2.TestCase):

    def test_indent_if(self):
        js_code = 'if (x == true) {\n\tif (y == true) {\n\t\tconsole.log("y and x are true")\n\t}\n}'
        py_code = 'if (x == True):\n\tif (y == True):\n\t\tprint("y and x are true")'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py')['translation']['output_code'])
        self.assertEqual(js_code, main.main(py_code, 'py', 'js')['translation']['output_code'])

    def test_indent_for_of(self):
        js_code = 'for (j of [1, 2]) {\n\tfor (k of [3, 4]) {\n\t\tj\n\t\tk\n\t}\n}'
        py_code = 'for j in [1, 2]:\n\tfor k in [3, 4]:\n\t\tj\n\t\tk'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py')['translation']['output_code'])
        self.assertEqual(js_code, main.main(py_code, 'py', 'js')['translation']['output_code'])

    def test_indent_for_range(self):
        js_code = 'for (let j = 0; j < 10; j += 1) {\n\tfor (let k = 20; k < 30; k += 1) {\n\t\tj\n\t\tk\n\t}\n}'
        py_code = 'for j in range (0, 10, 1):\n\tfor k in range (20, 30, 1):\n\t\tj\n\t\tk'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py')['translation']['output_code'])
        self.assertEqual(js_code, main.main(py_code, 'py', 'js')['translation']['output_code'])

    def test_indent_while(self):
        js_code = 'while (1) {\n\twhile (2) {\n\t\t3\n\t}\n}'
        py_code = 'while (1):\n\twhile (2):\n\t\t3'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py')['translation']['output_code'])
        self.assertEqual(js_code, main.main(py_code, 'py', 'js')['translation']['output_code'])

    def test_indent_func_and_if(self):
        js_code = 'function test() {\n\tif (1) {\n\t\t2\n\t}\n}'
        py_code = 'def test():\n\tif (1):\n\t\t2'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py')['translation']['output_code'])
        self.assertEqual(js_code, main.main(py_code, 'py', 'js')['translation']['output_code'])

    def test_indent_func_if_while_for(self):
        js_code = 'function test() {\n\tif (1) {\n\t\twhile (2) {\n\t\t\tfor (j of [3, 4]) {\n\t\t\t\t5\n\t\t\t}\n\t\t}\n\t}\n}'
        py_code = 'def test():\n\tif (1):\n\t\twhile (2):\n\t\t\tfor j in [3, 4]:\n\t\t\t\t5'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py')['translation']['output_code'])
        self.assertEqual(js_code, main.main(py_code, 'py', 'js')['translation']['output_code'])


if __name__ == '__main__':
    unittest2.main()
