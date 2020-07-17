import unittest2
import main

class TestJavaAssignment(unittest2.TestCase):
    def test_basic(self):
        code = 'int x = 1;\n String s = "s";\nboolean b = false;'
        self.assertEqual('int x = 1\nString s = "s"\nboolean b = false', main.main(code, 'java', 'java'))

if __name__ == '__main__':
    unittest2.main()