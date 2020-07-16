import unittest2
import main

class TestJavaPrim(unittest2.TestCase):
    def test_basic(self):
        code = 'myFunction()'
        self.assertEqual('myFunction()', main.main(code, 'java', 'java'))

if __name__ == '__main__':
    unittest2.main()