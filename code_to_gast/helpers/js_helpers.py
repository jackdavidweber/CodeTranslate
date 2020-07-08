import js_router

"""
handles arrays and recursively calls node_to_gast on all its elements
"""
def array_expression_to_gast(node):
    gast = {"type" : "arr"}
    gast["elements"] = []
    for elm in node.elements:
        gast["elements"].append(js_router.node_to_gast(elm))
    return gast

"""
handles dictionaries conversion to generic AST with list of properties
"""
def dictionary_to_gast(node):
    gast = {"type": "dict"}
    gast["elements"] = js_router.node_to_gast(node.properties)
    return gast

"""
takes each property of a dictionary and turns it into a property type
"""
def property_to_gast(node):
    gast = {"type": "property"}
    gast["key"] = js_router.node_to_gast(node.key)
    gast["value"] = js_router.node_to_gast(node.value)
    return gast

"""
takes ast node of type program and returns
a generic ast for that node
example print("hello"):
    node (input): Program(body=[ExpressionStatement(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))])
    gast (output): {'type': 'root', 'body': [{'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}]}
"""
def program_to_gast(node):
    gast = {"type": "root"}
    gast["body"] = js_router.node_to_gast(node.body)
    return gast

"""
converts a python ast BinOp and converts it to a gast node
"""
def bin_op_to_gast(bop):
  gast = {"type" : "binOp"}
  if bop.left.type != "BinaryExpression" and bop.right.type != "BinaryExpression":
      gast["left"] = js_router.node_to_gast(bop.left)
      gast["op"] = bop.operator
      gast["right"] = js_router.node_to_gast(bop.right)
  if bop.left.type == "BinaryExpression":
      gast["left"] = bin_op_to_gast(bop.left)
      gast["op"] = bop.operator
      gast["right"] = js_router.node_to_gast(bop.right)
  if bop.right.type == "BinaryExpression":
      gast["left"] = js_router.node_to_gast(bop.left)
      gast["op"] = bop.operator
      gast["right"] = bin_op_to_gast(bop.right)
  return gast

"""
takes a type boolean operator and turns it into our generic AST
"""
def bool_op_to_gast(node):
    gast = {"type": "boolOp"}
    gast["left"] = js_router.node_to_gast(node.left)
    gast["op"] = node.operator
    gast["right"] = js_router.node_to_gast(node.right)
    return gast

"""
Converts Member Expression to our generic AST recursively
Used for functions called on objects and std funcs like console.log
"""
def member_expression_to_gast(node):
  if node.object.name == "console" and node.property.name == "log":
    return {"type": "logStatement"}
  
  gast = {"value": js_router.node_to_gast(node.object)}
  func_name = node.property.name
  # The tool only currently supports the built in functions below 
  # TODO add other built in function translations
  if func_name == "push":
    gast["type"] = "builtInAttribute"
    gast["id"] = "appendStatement"
    return gast
  if func_name == "pop":
    gast["type"] = "builtInAttribute"
    gast["id"] = "popStatement"
    return gast
  gast["type"] = "attribute"
  gast["id"] = node.property.name
  return gast

"""
takes a node that represents a list of nodes.
returns a list of gast
example console.log("hello"):
    node (input):
    gast (output): [{'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}]
example array of strings:
    input: [Str(s='hello'), Str(s='world')]
    output:[{'type': 'str', 'value': 'hello'}, {'type': 'str', 'value': 'world'}]
"""
def node_list(node):
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(js_router.node_to_gast(node[i]))
    return gast_list

"""
Seems like this block statement type is called
whenever there are curly braces. Probably will need 
to end up making this function more robust.
"""
def block_statement_to_gast(node):
  return js_router.node_to_gast(node.body)


"""
Takes unary operation such as ! and converts it to generic AST
"""
def unary_to_gast(node):
    return {"type": "unaryOp", "op": node.operator, "arg": js_router.node_to_gast(node.argument)}

def return_statement_to_gast(node):
    return {"type": "returnStatement", "value": js_router.node_to_gast(node.argument)}

"""
Handles assignment patterns ie x = 3, used to set default values in functions
"""
def assign_pattern_to_gast(node):
    gast = {"type": "assignPattern"}
    gast["left"] = js_router.node_to_gast(node.left)
    gast["right"] = js_router.node_to_gast(node.right)
    return gast
