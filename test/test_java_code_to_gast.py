import unittest2
import java.code_to_gast.java_main as java_main
import gasts


class test_py_code_to_gast(unittest2.TestCase):
    maxDiff = None

    def test_ifs(self):
        code = 'if (true) {System.out.println("This is true");}'
        self.assertEqual(gasts.gast_if_log, java_main.java_to_gast(code))

    def test_else(self):
        code = 'if (1) {System.out.println("1 is true");} else {System.out.println("1 is NOT true");}'
        self.assertEqual(gasts.gast_else_log, java_main.java_to_gast(code))

    def test_elif(self):
        code = 'if (1) {System.out.println("1 is true");} else if (2) {System.out.println("2 is true"); System.out.println("second line");}'
        self.assertEqual(gasts.gast_elif_log, java_main.java_to_gast(code))

    def test_forRange(self):
        code = 'for (int i = 0; i < 10; i += 2) {\n\t5;\n}'
        self.assertEqual(gasts.gast_for_range,
                         java_main.java_to_gast(code)["body"][0])

    def test_forRange_negative(self):
        code = 'for (int i = -25; i > -50; i -= 5) {\n\t5;\n}'
        self.assertEqual(gasts.gast_for_range_negative,
                         java_main.java_to_gast(code))

    def test_forOf_with_arr(self):
        code = 'for (int elem : arr) {\n\t5;}'
        self.assertEqual(gasts.gast_for_of_arr, java_main.java_to_gast(code))


if __name__ == '__main__':
    unittest2.main()
