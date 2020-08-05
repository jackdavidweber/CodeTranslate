import unittest2
import shared.gast_to_code.gast_to_code_router as gtc
import java.gast_to_code.java_helpers as java_helpers
import gasts


class TestJavaGastToCode(unittest2.TestCase):
    # test primitives
    def test_primitive_str(self):
        code = '"hello world";'
        output = gtc.gast_to_code(gasts.gast_str, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_primitive_num(self):
        code = '47.47;'
        output = gtc.gast_to_code(gasts.gast_num, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_primitive_true(self):
        code = 'true;'
        output = gtc.gast_to_code(gasts.gast_true, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_primitive_false(self):
        code = 'false;'
        output = gtc.gast_to_code(gasts.gast_false, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    # test other types
    def test_binOp_add(self):
        code = '3 + 4;'
        output = gtc.gast_to_code(gasts.gast_binOp_add, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_binOp_bitwise(self):
        code = '1 & 3;'
        output = gtc.gast_to_code(gasts.gast_binOp_bitwise, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_binOp_add_sub_mult_div(self):
        code = '1 + 2 - 3 * 4 / 5;'
        output = gtc.gast_to_code(gasts.gast_binOp_add_sub_mult_div, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_boolOp_and(self):
        code = '$$E0$$;'
        output = gtc.gast_to_code(gasts.gast_boolOp_and, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_boolOp_or_and(self):
        code = '$$E1$$;'
        output = gtc.gast_to_code(gasts.gast_boolOp_or_and, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    # test logStatement
    def test_logStatement_bool(self):
        code = 'System.out.println(false);'
        output = gtc.gast_to_code(gasts.gast_logStatement_bool, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_logStatement_two_arguments(self):
        code = 'System.out.println("hello world", 5);'
        output = gtc.gast_to_code(gasts.gast_logStatement_two_args, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    # test varAssign
    def test_varAssign_let(self):
        code = 'int x = 5;'
        output = gtc.gast_to_code(gasts.gast_varAssign_let, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_varAssign_const(self):
        code = 'int x = 5;'
        output = gtc.gast_to_code(gasts.gast_varAssign_const, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    # test multiple items in body
    def test_multi_body(self):
        code = 'int x = 5;\nint x = 5;'
        output = gtc.gast_to_code(gasts.gast_multi_body, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_if(self):
        code = 'if (true) {\n\tSystem.out.println("This is true");\n}'
        output = gtc.gast_to_code(gasts.gast_if_log, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_else(self):
        code = 'if (1) {\n\tSystem.out.println("1 is true");\n} else {\n\tSystem.out.println("1 is NOT true");\n}'
        output = gtc.gast_to_code(gasts.gast_else_log, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_elif(self):
        code = 'if (1) {\n\tSystem.out.println("1 is true");\n} else if (2) {\n\tSystem.out.println("2 is true");\n\tSystem.out.println("second line");\n}'
        output = gtc.gast_to_code(gasts.gast_elif_log, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_forRange(self):
        code = 'for (int i = 0; i < 10; i += 2) {\n\t5;\n}'
        output = gtc.gast_to_code(gasts.gast_for_range, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_forOf(self):
        code = 'for (GenericType elem : {1, 2}) {\n\t5;\n}'
        output = gtc.gast_to_code(gasts.gast_for_of, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_indent_if(self):
        code = 'if (x == true) {\n\tif (y == true) {\n\t\tSystem.out.println("y and x are true");\n\t}\n}'
        output = gtc.gast_to_code(gasts.gast_indent_if, "java")
        self.assertEqual(code, java_helpers.java_linter(output))

    def test_indent_for_of(self):
        code = 'for (GenericType j : {1, 2}) {\n\tfor (GenericType k : {3, 4}) {\n\t\tj;\n\t\tk;\n\t}\n}'
        output = gtc.gast_to_code(gasts.gast_indent_for_of, "java")
        self.assertEqual(code, java_helpers.java_linter(output))


if __name__ == '__main__':
    unittest2.main()
