import unittest2
import main

class TestJavaPrim(unittest2.TestCase):
    def test_basic(self):
        code = "System.out.println();"
        self.assertEqual("System.out.println()", main.main(code, 'java', 'java'))
    def test_basic_args(self):
        code = 'System.out.println("s");\n 1;'
        self.assertEqual('System.out.println("s")\n1', main.main(code, 'java', 'java'))
    def test_basic_var_declaration(self):
        code = 'int x = 1;\n String s = "s";\nboolean b = false;'
        self.assertEqual('int x = 1\nString s = "s"\nboolean b = false', main.main(code, 'java', 'java'))
if __name__ == '__main__':
    unittest2.main()