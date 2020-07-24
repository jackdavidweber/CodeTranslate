import unittest2
import translate


# TODO (swalsh15) this doesn't seem like it is testing just primitives?
class TestJavaPrim(unittest2.TestCase):

    def test_basic(self):
        code = "System.out.println();"
        self.assertEqual("System.out.println();",
                         translate.translate(code, 'java', 'java'))

    def test_basic_args(self):
        code = 'System.out.println("s");'
        self.assertEqual('System.out.println("s");',
                         translate.translate(code, 'java', 'java'))


if __name__ == '__main__':
    unittest2.main()
