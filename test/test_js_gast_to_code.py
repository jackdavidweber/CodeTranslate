import unittest2
import shared.gast_to_code.gast_to_code_router as gtc
import gasts


class TestJsGastToCode(unittest2.TestCase):
    # test primitives
    def test_primitive_str(self):
        code = '"hello world"'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_str, "js"))

    def test_primitive_num(self):
        code = '47.47'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_num, "js"))

    def test_primitive_true(self):
        code = 'true'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_true, "js"))

    def test_primitive_false(self):
        code = 'false'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_false, "js"))

    # test other types
    def test_nested_arr(self):
        code = '["hello", [1, 2]]'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_arr, "js"))

    def test_binOp_add(self):
        code = '3 + 4'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_add, "js"))

    def test_binOp_bitwise(self):
        code = '1 & 3'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_bitwise, "js"))

    def test_binOp_add_sub_mult_div(self):
        code = '1 + 2 - 3 * 4 / 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_binOp_add_sub_mult_div, "js"))

    def test_boolOp_and(self):
        code = 'true && false'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_boolOp_and, "js"))

    def test_boolOp_or_and(self):
        code = 'true || false && 4'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_boolOp_or_and, "js"))

    # test logStatement
    def test_logStatement_bool(self):
        code = 'console.log(false)'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_logStatement_bool, "js"))

    def test_logStatement_two_arguments(self):
        code = 'console.log("hello world", 5)'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_logStatement_two_args, "js"))

    # test varAssign
    def test_varAssign_let(self):
        code = 'let x = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_varAssign_let, "js"))

    def test_varAssign_const(self):
        code = 'const x = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_varAssign_const, "js"))

    # test multiple items in body
    def test_multi_body(self):
        code = 'const x = 5\nconst x = 5'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_multi_body, "js"))

    def test_if(self):
        code = 'if (true) {\n\tconsole.log("This is true")\n}'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_if_log, "js"))

    def test_else(self):
        code = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_else_log, "js"))

    def test_elif(self):
        code = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_elif_log, "js"))

    def test_forRange(self):
        code = 'for (let i = 0; i < 10; i += 2) {\n\t5\n}'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_for_range, "js"))

    def test_forOf(self):
        code = 'for (elem of [1, 2]) {\n\t5\n}'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_for_of, "js"))
    
    def test_indent_if(self):
        code = 'if (x == true) {\n\tif (y == true) {\n\t\tconsole.log("y and x are true")\n\t}\n}'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_indent_if, "js"))

    def test_indent_for_of(self):
        code = 'for (j of [1, 2]) {\n\tfor (k of [3, 4]) {\n\t\tj\n\t\tk\n\t}\n}'
        self.assertEqual(code, gtc.gast_to_code(gasts.gast_indent_for_of, "js"))


if __name__ == '__main__':
    unittest2.main()
