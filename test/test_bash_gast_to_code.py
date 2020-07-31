import unittest2
import shared.gast_to_code.gast_to_code_router as gtc
import gasts


class TestBashGastToCode(unittest2.TestCase):
    # test primitives
    def test_primitive_str(self):
        code = '"hello world"'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_str, "bash"))

    def test_primitive_num(self):
        code = '47.47'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_num, "bash"))

    def test_primitive_true(self):
        code = '$$E11$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_true, "bash"))

    def test_primitive_false(self):
        code = '$$E10$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_false, "bash"))

    # test other types
    def test_nested_arr(self):
        code = '$$E9$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_arr, "bash"))

    def test_binOp_add(self):
        code = '3 + 4'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_add, "bash"))

    def test_binOp_bitwise(self):
        code = '1 & 3'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_bitwise, "bash"))

    def test_binOp_add_sub_mult_div(self):
        code = '1 + 2 - 3 * 4 / 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_add_sub_mult_div, "bash"))

    def test_boolOp_and(self):
        code = '$$E0$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_boolOp_and, "bash"))

    def test_boolOp_or_and(self):
        code = '$$E1$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_boolOp_or_and, "bash"))

    # test logStatement
    def test_logStatement_bool(self):
        code = 'echo $$E8$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_logStatement_bool, "bash"))

    def test_logStatement_two_arguments(self):
        code = 'echo "hello world" 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_logStatement_two_args, "bash"))

    # test varAssign
    def test_varAssign_let(self):
        code = 'x = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_varAssign_let, "bash"))

    def test_varAssign_const(self):
        code = 'x = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_varAssign_const, "bash"))

    # test multiple items in body
    def test_multi_body(self):
        code = 'x = 5\nx = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_multi_body, "bash"))

    def test_if(self):
        code = 'if [[ $$E4$$ ]]; then\n\techo "This is true"\nfi'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_if_log, "bash"))

    def test_else(self):
        code = 'if [[ 1 ]]; then\n\techo "1 is true"\nelse\n\techo "1 is NOT true"\nfi'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_else_log, "bash"))

    def test_elif(self):
        code = 'if [[ 1 ]]; then\n\techo "1 is true"\nelif [[ 2 ]]; then\n\techo "2 is true"\n\techo "second line"\nfi'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_elif_log, "bash"))

    def test_forRange(self):
        code = '$$E3$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_for_range, "bash"))

    def test_forOf(self):
        code = '$$E2$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_for_of, "bash"))
    
    def test_indent_if(self):
        code = 'if [[ x == $$E6$$ ]]; then\n\tif [[ y == $$E7$$ ]]; then\n\t\techo "y and x are true"\n\tfi\nfi'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_indent_if, "bash"))

    def test_indent_for_of(self):
        code = '$$E5$$'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_indent_for_of, "bash"))


if __name__ == '__main__':
    unittest2.main()
