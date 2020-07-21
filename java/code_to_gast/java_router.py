import javalang.tree
import java.code_to_gast.java_expression as java_expression
import java.code_to_gast.java_helpers as java_helpers
import java.code_to_gast.java_assign as java_assign
import java.code_to_gast.java_conditional as java_conditional
import java.code_to_gast.java_loop as java_loop


def node_to_gast(node):
    #base cases
    if type(node) == javalang.tree.Literal:
        # node.value is stored as string in java AST
        if node.value.isnumeric():
            # TODO add in float type to generic AST (Ticket #152)
            return java_helpers.int_to_gast(node)
        if node.value.startswith('"'):
            return {"type": "str", "value": node.value.replace('"', '')}
        elif node.value == "true":
            return {"type": "bool", "value": 1}
        elif node.value == "false":
            return {"type": "bool", "value": 0}
        else:
            return "Unsupported prim"
    elif type(node) == str:
        return {"type": "name", "value": node}
    elif node == None:
        return {"type": "none"}
    elif type(node) == javalang.tree.BinaryOperation:
        return java_helpers.bin_op_to_gast(node)
    elif type(node) == javalang.tree.MethodInvocation:
        return java_expression.method_invocation_to_gast(node)
    elif type(node) == javalang.tree.CompilationUnit:
        # only support for one class currently
        return node_to_gast(node.types[0])
    elif type(node) == javalang.tree.ClassDeclaration:
        return java_expression.class_declaration_to_gast(node)
    elif type(node) == javalang.tree.MethodDeclaration:
        return node_to_gast(node.body)
    elif type(node) == javalang.tree.StatementExpression:
        return node_to_gast(node.expression)
    elif type(node) == list:
        return java_helpers.node_list_to_gast_list(node)
    elif type(node) == javalang.tree.IfStatement:
        return java_conditional.if_to_gast(node)
    elif type(node) == javalang.tree.BlockStatement:
        return node_to_gast(node.statements)
    elif type(node) == javalang.tree.LocalVariableDeclaration:
        # our current gAST doesn't support multiple declarations
        if len(node.declarators) == 1:
            return node_to_gast(node.declarators[0])
        else:
            return {"type": "error", "value": "unsupported"}
    elif type(node) == javalang.tree.VariableDeclarator:
        return java_assign.assign_to_gast(node)
    elif type(node) == javalang.tree.VariableDeclaration:
        return node_to_gast(node.declarators[0])
    elif type(node) == javalang.tree.MemberReference:
        return java_assign.member_reference_to_gast(node)
    elif type(node) == javalang.tree.ArrayInitializer:
        return java_helpers.array_to_gast(node.initializers)
    elif type(node) == javalang.tree.ForStatement:
        return java_loop.for_loop_to_gast(node)
    elif type(node) == javalang.tree.Assignment:
        return java_assign.aug_assign_to_gast(node)
    else:
        # not supported
        return {"type": "error", "value": "unsupported"}
