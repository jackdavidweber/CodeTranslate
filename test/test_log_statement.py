import unittest2
import translate


class TestLogStatement(unittest2.TestCase):

    def test_no_args(self):
        self.assertEqual('console.log()',
                         translate.translate('print()', 'py', 'js'))
        self.assertEqual('print()',
                         translate.translate('console.log()', 'js', 'py'))

    def test_one_arg(self):
        self.assertEqual('console.log("hello")',
                         translate.translate('print("hello")', 'py', 'js'))
        self.assertEqual('print(5)',
                         translate.translate('console.log(5)', 'js', 'py'))
        self.assertEqual('echo 8',
                         translate.translate('console.log(8)', 'js', 'bash'))

    def test_quotes_string(self):
        self.assertEqual(
            'print("working")',
            translate.translate('console.log("working")', 'js', 'py'))

    def test_arrays(self):
        self.assertEqual(
            'print([[1, 3], [3, 4]])',
            translate.translate('console.log([[1, 3], [3,4]])', 'js', 'py'))
        self.assertEqual(
            'console.log(["hi", "bye"])',
            translate.translate('print(["hi", "bye"])', 'py', 'js'))

    def test_boolean(self):
        self.assertEqual('print(True)',
                         translate.translate('console.log(true)', 'js', 'py'))
        self.assertEqual('console.log(!false)',
                         translate.translate('print(not False)', 'py', 'js'))

    def test_none(self):
        self.assertEqual('console.log(null)',
                         translate.translate('print(None)', 'py', 'js'))
        self.assertEqual('print(None)',
                         translate.translate('console.log(null)', 'js', 'py'))


if __name__ == '__main__':
    unittest2.main()
