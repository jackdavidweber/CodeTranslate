import javalang.tree
import java.code_to_gast.java_expression as java_expression

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
            return "Unsupported prim"
    elif type(node) == javalang.tree.MethodInvocation:
        return java_expression.method_invocation_to_gast(node)
    elif type(node) == javalang.tree.CompilationUnit:
        # only support for one class currently
        #FIXME: only one statement support 
        return node_to_gast(node.types[0])
    elif type(node) == javalang.tree.ClassDeclaration:
        gast = {"type": "root"}
        gast["body"] = node_to_gast(node.body)
        return gast
    elif type(node) == javalang.tree.MethodDeclaration:
        # only supports one function currently
        return node_to_gast(node.body[0])
    elif type(node) == javalang.tree.StatementExpression:
        return node_to_gast(node.expression)
    elif type(node) == list:
        #TODO: make helper function
        #NOTE: since ignoring parts for classes/funcs creating lists inside empty lists
        gast_list = []
        for i in range(0, len(node)):
            gast_list.append(node_to_gast(node[i]))
        return gast_list
    else:   
        # not supported
        return {"type": "error", "value": "unsupported"}
    