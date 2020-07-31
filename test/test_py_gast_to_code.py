import unittest2
import shared.gast_to_code.gast_to_code_router as gtc
import gasts


class TestPyGastToCode(unittest2.TestCase):
    # test primitives
    def test_primitive_str(self):
        code = '"hello world"'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_str, "py"))

    def test_primitive_num(self):
        code = '47.47'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_num, "py"))

    def test_primitive_true(self):
        code = 'True'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_true, "py"))

    def test_primitive_false(self):
        code = 'False'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_false, "py"))

    # test other types
    def test_nested_arr(self):
        code = '["hello", [1, 2]]'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_arr, "py"))

    def test_binOp_add(self):
        code = '3 + 4'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_add, "py"))

    def test_binOp_bitwise(self):
        code = '1 & 3'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_bitwise, "py"))

    def test_binOp_add_sub_mult_div(self):
        code = '1 + 2 - 3 * 4 / 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_add_sub_mult_div, "py"))

    def test_boolOp_and(self):
        code = 'True and False'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_boolOp_and, "py"))

    def test_boolOp_or_and(self):
        code = 'True or False and 4'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_boolOp_or_and, "py"))

    # test logStatement
    def test_logStatement_bool(self):
        code = 'print(False)'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_logStatement_bool, "py"))

    def test_logStatement_two_arguments(self):
        code = 'print("hello world", 5)'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_logStatement_two_args, "py"))

    # test varAssign
    def test_varAssign_let(self):
        code = 'x = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_varAssign_let, "py"))

    def test_varAssign_const(self):
        code = 'x = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_varAssign_const, "py"))

    # test multiple items in body
    def test_multi_body(self):
        code = 'x = 5\nx = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_multi_body, "py"))

    def test_if(self):
        code = 'if (True):\n\tprint("This is true")'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_if_log, "py"))

    def test_else(self):
        code = 'if (1):\n\tprint("1 is true")\nelse:\n\tprint("1 is NOT true")'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_else_log, "py"))

    def test_elif(self):
        code = 'if (1):\n\tprint("1 is true")\nelif (2):\n\tprint("2 is true")\n\tprint("second line")'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_elif_log, "py"))

    def test_forRange(self):
        code = 'for i in range (0, 10, 2):\n\t5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_for_range, "py"))

    def test_forOf(self):
        code = 'for elem in [1, 2]:\n\t5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_for_of, "py"))
    
    def test_indent_if(self):
        code = 'if (x == True):\n\tif (y == True):\n\t\tprint("y and x are true")'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_indent_if, "py"))

    def test_indent_for_of(self):
        code = 'for j in [1, 2]:\n\tfor k in [3, 4]:\n\t\tj\n\t\tk'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_indent_for_of, "py"))


if __name__ == '__main__':
    unittest2.main()
