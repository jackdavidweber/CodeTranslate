import unittest2
import translate


class TestVarAssign(unittest2.TestCase):

    def test_string_assign(self):
        self.assertEqual('x = "hi"',
                         translate.translate('let x = "hi"', 'js', 'py'))
        self.assertEqual('let test = "working"',
                         translate.translate('test = "working"', 'py', 'js'))
        self.assertEqual('test="working"',
                         translate.translate('test = "working"', 'py', 'bash'))

    def test_int_assign(self):
        self.assertEqual('num = 109',
                         translate.translate('const num = 109', 'js', 'py'))
        self.assertEqual('let n = 12',
                         translate.translate('n = 12', 'py', 'js'))
        self.assertEqual('n=12', translate.translate('n = 12', 'py', 'bash'))

    def test_array_assign(self):
        self.assertEqual('arr = [3, 6]',
                         translate.translate('let arr = [3, 6]', 'js', 'py'))
        self.assertEqual(
            'let nest = [[1, 9], [2, 8]]',
            translate.translate('nest = [[1,9],[2,8]]', 'py', 'js'))

    def test_boolean_assign(self):
        self.assertEqual('boo = not True',
                         translate.translate('const boo=!true', 'js', 'py'))
        self.assertEqual('let lean = false',
                         translate.translate('lean = False', 'py', 'js'))

    def test_none_assign(self):
        self.assertEqual('no = None',
                         translate.translate('let no =null', 'js', 'py'))
        self.assertEqual('let help = null',
                         translate.translate('help = None', 'py', 'js'))

    def test_aug_assign_minus(self):
        self.assertEqual('x -= 1', translate.translate('x -= 1', 'js', 'py'))
        self.assertEqual('y -= 3', translate.translate('y-=3', 'py', 'js'))
        self.assertEqual('z -= 3', translate.translate('z-=3;', 'java', 'py'))

    def test_aug_assign_mult(self):
        self.assertEqual('hi *= 5', translate.translate('hi *= 5', 'js', 'py'))
        self.assertEqual('y *= 4', translate.translate('y*=4', 'py', 'js'))
        self.assertEqual('z *= 8', translate.translate('z*=8;', 'java', 'js'))

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
