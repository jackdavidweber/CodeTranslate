import unittest2
import translate


class TestJavaAssignment(unittest2.TestCase):

    def test_basic(self):
        code = 'int x = 1;\n String s = "s";\nboolean b = false;'
        self.assertEqual('int x = 1;\nString s = "s";\nboolean b = false;',
                         translate.translate(code, 'java', 'java'))

    def test_arr(self):
        self.assertEqual('int[] x = {1, 2};',
                         translate.translate('int[] x = {1, 2};', 'java', 'java'))


if __name__ == '__main__':
    unittest2.main()
