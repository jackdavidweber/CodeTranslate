import unittest2
import python.code_to_gast.py_main as py_main
import gasts


class test_py_code_to_gast(unittest2.TestCase):
    maxDiff = None

    def test_ifs(self):
        code = 'if (True):\n\tprint("This is true")'
        self.assertEqual(gasts.gast_if_log, py_main.py_to_gast(code))

    def test_else(self):
        code = 'if (1):\n\tprint("1 is true")\nelse:\n\tprint("1 is NOT true")\n'
        self.assertEqual(gasts.gast_else_log, py_main.py_to_gast(code))

    def test_elif(self):
        code = 'if (1):\n\tprint("1 is true")\nelif (2):\n\tprint("2 is true")\n\tprint("second line")\n'
        self.assertEqual(gasts.gast_elif_log, py_main.py_to_gast(code))

    def test_forRange(self):
        code = 'for i in range (0, 10, 2):\n\t5'
        self.assertEqual(gasts.gast_for_range, py_main.py_to_gast(code)["body"][0])

    def test_forRange_negative(self):
        code = 'for i in range (-25, -50, -5):\n\t5'
        self.assertEqual(gasts.gast_for_range_negative, py_main.py_to_gast(code))

    def test_forOf(self):
        code = 'for elem in [1, 2]:\n\t5'
        self.assertEqual(gasts.gast_for_of, py_main.py_to_gast(code)["body"][0])

    def test_forOf_with_arr(self):
        code = 'for elem in arr:\n\t5'
        self.assertEqual(gasts.gast_for_of_arr, py_main.py_to_gast(code))

if __name__ == '__main__':
    unittest2.main()
