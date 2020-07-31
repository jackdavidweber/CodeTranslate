import unittest2
import javascript.code_to_gast.js_main as js_main
import gasts


class test_py_code_to_gast(unittest2.TestCase):
    maxDiff = None

    def test_ifs(self):
        code = 'if (true) {\n\tconsole.log("This is true")\n}'
        self.assertEqual(gasts.gast_if_log, js_main.js_to_gast(code))

    def test_else(self):
        code = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}' 
        self.assertEqual(gasts.gast_else_log, js_main.js_to_gast(code))

    def test_elif(self):
        code = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'
        self.assertEqual(gasts.gast_elif_log, js_main.js_to_gast(code))

    def test_forRange(self):
        code = 'for (let i = 0; i < 10; i += 2) {\n\t5\n}'
        self.assertEqual(gasts.gast_for_range, js_main.js_to_gast(code)["body"][0])

    def test_forRange_negative(self):
        code = 'for (let i = -25; i > -50; i -= 5) {\n\t5\n}'
        self.assertEqual(gasts.gast_for_range_negative, js_main.js_to_gast(code))

    def test_forOf(self):
        code = 'for (elem of [1, 2]) {\n\t5\n}'
        self.assertEqual(gasts.gast_for_of, js_main.js_to_gast(code)["body"][0])

    def test_forOf_with_arr(self):
        code = 'for (elem of arr) {\n\t5\n}'
        self.assertEqual(gasts.gast_for_of_arr, js_main.js_to_gast(code))

if __name__ == '__main__':
    unittest2.main()
