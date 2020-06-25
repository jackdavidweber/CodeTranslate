import js_router

#TODO: handling of booleans (have type literal)
def jsarg_to_str(arg):
  if arg.type == "Literal":
    return arg.value
  elif arg.type == "Identifier":
    #identifier has quotes around name
    return arg.name
  elif arg.type == "BinaryExpression":
    return binOp_to_str(arg)
  elif arg.type == "ArrayExpression":
    arg_list = []
    for elm in arg.elements:
        arg_list.append(jsarg_to_str(elm))
    return arg_list
  else:
    return ""

"""
takes ast node of type program and returns
a generic ast for that node
example print("hello"):
    node (input): Program(body=[ExpressionStatement(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))])
    gast (output): {'type': 'root', 'body': [{'type': 'logStatement', 'args': ['hello']}]}
"""
def program_to_gast(node):
    gast = {"type": "root"}
    gast["body"] = js_router.node_to_gast(node.body)
    return gast

"""
converts a python ast BinOp and converts it to a readable string recursively 
"""
def binOp_to_str(bop):
  if bop.left.type == "BinaryExpression":
    s = binOp_to_str(bop.left) + bop.operator + bop.right.raw
  else:
    # base case: if left is just a number, operate on left wrt right
    s = bop.left.raw + bop.operator + bop.right.raw
  return s

"""
Converts Member Expression and converts to readable string recursively
Used for functions called on objects and std funcs like console.log
"""
def memExp_to_str(node):
  #base case: object is literal
  if node.object.type == "MemberExpression":
    s = memExp_to_str(node.object) + '.' + node.property.name
  else:
    s = node.object.name + '.' + node.property.name
  return s

"""
takes list of arguments in js ast and converts them to a list of
strings
"""
def jsargs_to_strlist(args):
  out = []
  for arg in args:
    out.append(jsarg_to_str(arg))
  return out

"""
takes a node that represents a list of nodes.
returns a list of gast
example console.log("hello"):
    node (input):
    gast (output): [{'type': 'logStatement', 'args': ['hello']}]
example array of strings:
    input: [Str(s='hello'), Str(s='world')]
    output:['hello', 'world']
"""
def node_list(node):
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(js_router.node_to_gast(node[i]))
    return gast_list
