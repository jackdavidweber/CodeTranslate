import unittest2
import main


# TODO (swalsh15) this doesn't seem like it is testing just primitives?
class TestJavaPrim(unittest2.TestCase):

    def test_basic(self):
        code = "System.out.println();"
        self.assertEqual("System.out.println();",
                         main.main(code, 'java', 'java')['translation']['output_code'])

    def test_basic_args(self):
        code = 'System.out.println("s");'
        self.assertEqual('System.out.println("s");',
                         main.main(code, 'java', 'java')['translation']['output_code'])


if __name__ == '__main__':
    unittest2.main()
