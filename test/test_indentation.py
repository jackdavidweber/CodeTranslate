import unittest2
import main

class TestIndentation(unittest2.TestCase):
    def test_indent_if(self):
        js_code = 'if (x == true) {\n\tif (y == true) {\n\t\tconsole.log("y and x are true")\n\t}\n}'
        py_code = 'if (x == True):\n\tif (y == True):\n\t\tprint("y and x are true")'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_indent_for_of(self):
        js_code = 'for (j of [1, 2]) {\n\tfor (k of [3, 4]) {\n\t\tj\n\t\tk\n\t}\n}'
        py_code = 'for j in [1, 2]:\n\tfor k in [3, 4]:\n\t\tj\n\t\tk'

        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()