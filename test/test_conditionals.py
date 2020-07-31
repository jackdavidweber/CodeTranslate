import unittest2
import test_matrix


class TestConditionals(unittest2.TestCase):

    def test_if(self):
        js_code = 'if (1) {\n\tconsole.log("This is true")\n}'
        py_code = 'if (1):\n\tprint("This is true")'
        bash_code = 'if [[ 1 ]]; then\n\techo "This is true"\nfi'
        java_code = 'if (1) {\n\tSystem.out.println("This is true");\n}'
        test_matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_else(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}'  # TODO: consider adding ; after console.log()
        py_code = 'if (1):\n\tprint("1 is true")\nelse:\n\tprint("1 is NOT true")'
        bash_code = 'if [[ 1 ]]; then\n\techo "1 is true"\nelse\n\techo "1 is NOT true"\nfi'
        java_code = 'if (1) {\n\tSystem.out.println("1 is true");\n} else {\n\tSystem.out.println("1 is NOT true");\n}'
        test_matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_elif(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'
        py_code = 'if (1):\n\tprint("1 is true")\nelif (2):\n\tprint("2 is true")\n\tprint("second line")'
        java_code = 'if (1) {\n\tSystem.out.println("1 is true");\n} else if (2) {\n\tSystem.out.println("2 is true");\n\tSystem.out.println("second line");\n}'
        test_matrix.test(self, py_code, js_code, java_code)

    def test_elif_else(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n} else {\n\tconsole.log("nothing is true")\n}'
        py_code = 'if (1):\n\tprint("1 is true")\nelif (2):\n\tprint("2 is true")\nelse:\n\tprint("nothing is true")'
        bash_code = 'if [[ 1 ]]; then\n\techo "1 is true"\nelif [[ 2 ]]; then\n\techo "2 is true"\nelse\n\techo "nothing is true"\nfi'
        java_code = 'if (1) {\n\tSystem.out.println("1 is true");\n} else if (2) {\n\tSystem.out.println("2 is true");\n} else {\n\tSystem.out.println("nothing is true");\n}'
        test_matrix.test(self, py_code, js_code, java_code, bash_code)


if __name__ == '__main__':
    unittest2.main()
