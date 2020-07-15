import javalang.tree
import java.code_to_gast.java_expression as java_expression
import java.code_to_gast.java_helpers as java_helpers

def node_to_gast(node):
    #base cases
    if type(node) == javalang.tree.Literal:
        # node.value is stored as string in java AST
        if node.value.isnumeric():
            return {"type": "num", "value": node.value}
        if node.value.startswith('"'):
            return {"type": "str", "value": node.value.replace('"', '')}
        elif node.value == "true":
            return {"type": "bool", "value": 1}
        elif node.value == "false":
            return {"type": "bool", "value": 0}
        else:
            return "Unsupported primitive"
    
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
    else:   
        # not supported
        return {"type": "error", "value": "unsupported"}
    