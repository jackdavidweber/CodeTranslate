import esprima
import ast 

program = 'const x = [1, "ste", x]\n console.log("i love lucy")'

# tokens parses each character and classifies it - may be usefu;
#tokens = esprima.tokenize(program)


"""
Takes javascript expressions and converts them to the generic
ast format
"""
def jsexpr_to_gast(node):
  gast = {}
  if node.type == "CallExpression":
    # handle callee
    if node.callee.type == "MemberExpression":
      if (memExp_to_str(node.callee) == "console.log"):
        gast["type"] = "logStatement"
      else: 
        gast["type"] = "customStatement"
    else:
      gast["type"] = "customStatement"
    
    # handle args
    gast["args"] = jsargs_to_strlist(node.arguments)
  return gast

"""
Handles js var declerations to generic AST node
"""
def jsassign_to_gast(node):
  gast = {}
  gast["type"] = "varAssign"

  # only works with single assignment
  gast["varId"] = node[0].id.name
  gast["varValue"] = jsarg_to_str(node[0].init) 
  return gast

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
Takes js and converts to generic ast 
"""
def js_to_gast(program):
    input_ast =  esprima.parseScript(program, { "tokens": True })
    # TODO: can add more fields to the generic ast
    gast = {"type": "root", "body": []}

    # NOTE: with current implementation, it will just go until it sees something it recognizes
    # eventually can implement nested structures
    for node in input_ast.body:
      if node.type == "ExpressionStatement":
        gast["body"].append(jsexpr_to_gast(node.expression))
      if node.type == "VariableDeclaration":
        gast["body"].append(jsassign_to_gast(node.declarations))
    return gast


print(js_to_gast(program))