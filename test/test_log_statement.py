import unittest2
import main


class TestLogStatement(unittest2.TestCase):

    def test_no_args(self):
        self.assertEqual('console.log()', main.main('print()', 'py', 'js'))
        self.assertEqual('print()', main.main('console.log()', 'js', 'py'))

    def test_one_arg(self):
        self.assertEqual('console.log("hello")',
                         main.main('print("hello")', 'py', 'js'))
        self.assertEqual('print(5)', main.main('console.log(5)', 'js', 'py'))
        self.assertEqual('echo 8', main.main('console.log(8)', 'js', 'bash'))

    def test_quotes_string(self):
        self.assertEqual('print("working")',
                         main.main('console.log("working")', 'js', 'py'))

    def test_arrays(self):
        self.assertEqual('print([[1, 3], [3, 4]])',
                         main.main('console.log([[1, 3], [3,4]])', 'js', 'py'))
        self.assertEqual('console.log(["hi", "bye"])',
                         main.main('print(["hi", "bye"])', 'py', 'js'))

    def test_boolean(self):
        self.assertEqual('print(True)',
                         main.main('console.log(true)', 'js', 'py'))
        self.assertEqual('console.log(!false)',
                         main.main('print(not False)', 'py', 'js'))

    def test_none(self):
        self.assertEqual('console.log(null)',
                         main.main('print(None)', 'py', 'js'))
        self.assertEqual('print(None)',
                         main.main('console.log(null)', 'js', 'py'))


if __name__ == '__main__':
    unittest2.main()
