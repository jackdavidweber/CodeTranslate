import ast
import python.code_to_gast.py_helpers as helpers
import python.code_to_gast.py_expression as expression
import python.code_to_gast.py_assign as assign
import python.code_to_gast.py_conditional as conditional
import python.code_to_gast.py_loop as loop


def node_to_gast(node):
    """
    router that all nodes in the python AST are passed through recursively
    """
    # Base Cases
    if type(node) == ast.Str:
        return helpers.string_to_gast(node)
    elif type(node) == ast.Num:
        return helpers.num_to_gast(node)
    elif type(node) == ast.NameConstant:
        return helpers.name_constant_to_gast(node)
    elif type(node) == ast.arg:
        return helpers.arg_to_gast(node)
    elif type(node) == str:
        return helpers.str_to_gast(node)
    elif type(node) == ast.Break:
        return helpers.break_to_gast(node)
    elif type(node) == ast.Continue:
        return helpers.continue_to_gast(node)

    # Helpers
    elif type(node) == ast.Module:
        return helpers.module_to_gast(node)
    elif type(node) == ast.BinOp:
        return helpers.bin_op_to_gast(node)
    elif type(node) == ast.BoolOp:
        return helpers.bool_op_to_gast(node)
    elif type(node) == ast.List:
        return helpers.array_to_gast(node)
    elif type(node) == ast.Dict:
        return helpers.dictionary_to_gast(node)
    elif type(node) == list:  # TODO: break this up into diff section
        return helpers.node_list_to_gast(node)
    elif type(node) == ast.Name:
        return helpers.name_to_gast(node)
    elif type(node) == ast.UnaryOp:
        return helpers.unary_op_to_gast(node)
    elif type(node) == ast.Compare:
        return helpers.compare_to_gast(node)

    # Expressions
    elif type(node) == ast.Expr:
        return expression.expr_to_gast(node)
    elif type(node) == ast.Call:
        return expression.call_to_gast(node)
    elif type(node) == ast.Attribute:
        return expression.attribute_to_gast(node)
    elif type(node) == ast.FunctionDef:
        return expression.function_def_to_gast(node)
    elif type(node) == ast.Subscript:
        return expression.subscript_to_gast(node)
    elif type(node) == ast.arguments:
        return helpers.function_args_to_gast(node)
    elif type(node) == ast.Lambda:
        return expression.lamda_to_gast(node)
    # Assigns
    elif type(node) == ast.Assign:
        return assign.assign_to_gast(node)
    elif type(node) == ast.AugAssign:
        return assign.aug_assign_to_gast(node)

    # Conditionals
    elif type(node) == ast.If:
        return conditional.if_statement_to_gast(node)

    elif type(node) == ast.Return:
        return helpers.return_statement_to_gast(node)
    # Loops
    elif type(node) == ast.While:
        return loop.while_statement_to_gast(node)
    elif type(node) == ast.For:
        return loop.for_statement_to_gast(node)

    else:
        return {"type": "error", "value": "unsupported"}
