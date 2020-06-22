import esprima
import ast 

program = 'console.log("el" + 1)'

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
    if node.callee.object.name == "console" and node.callee.property.name == "log":
      gast["type"] = "logStatement"
    else:
      #TODO recursive handling of callee
      gast["type"] = "customStatement"
    # handle args
    gast["args"] = jsargs_to_strlist(node.arguments)
  return gast

def jsarg_to_str(arg):
  if arg.type == "Literal":
    return arg.value
  elif arg.type == "Identifier":
    return arg.name
  elif arg.type == "BinaryExpression":
    return binOp_to_str(arg)
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
    
    return gast


print(js_to_gast(program))