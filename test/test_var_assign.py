import unittest2
import translate
import matrix


class TestVarAssign(unittest2.TestCase):

    def test_string_assign(self):
        py_code = 'x = "hi"'
        js_code = 'let x = "hi"'
        bash_code = 'x = "hi"'
        java_code = 'String x = "hi";'
        matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_int_assign(self):
        py_code = 'num = 109'
        js_code = 'let num = 109'
        bash_code = 'num = 109'
        java_code = 'int num = 109;'
        matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_array_assign(self):
        py_code = 'arr = [3, 6]'
        js_code = 'let arr = [3, 6]'
        bash_code = 'arr = (3, 6)'
        java_code = 'int[] arr = {3, 6};'
        matrix.test(self, py_code, js_code, java_code, bash_code)

    def test_nested_array_assign(self):
        py_code = 'arr = [[1, 9], [2, 8]]'
        js_code = 'let arr = [[1, 9], [2, 8]]'
        matrix.test(self, py_code, js_code)

    def test_boolean_assign(self):
        py_code = 'boo = True'
        js_code = 'let boo = true'
        java_code = 'boolean boo = true;'
        matrix.test(self, py_code, js_code, java_code)

    def test_none_assign(self):
        py_code = 'no = None'
        js_code = 'let no = null'
        matrix.test(self, py_code, js_code)

    def test_aug_assign_minus(self):
        py_code = 'x -= 1'
        js_code = 'x -= 1'
        java_code = 'x -= 1;'
        matrix.test(self, py_code, js_code, java_code)

    def test_aug_assign_mult(self):
        py_code = 'hi *= 5'
        js_code = 'hi *= 5'
        java_code = 'hi *= 5;'
        matrix.test(self, py_code, js_code, java_code)

    def test_update_expression(self):
        output_py_code = "x += 1"
        js_code = "x++"
        bash_code = "x++"
        java_code = "x++;"
        self.assertEqual(output_py_code,
                         translate.translate(js_code, "js", "py"))
        self.assertEqual(bash_code,
                         translate.translate(java_code, "java", "bash"))
        self.assertEqual(bash_code, translate.translate(js_code, "js", "bash"))
        self.assertEqual(java_code, translate.translate(js_code, "js", "java"))
        self.assertEqual(bash_code,
                         translate.translate(java_code, "java", "bash"))


if __name__ == '__main__':
    unittest2.main()
