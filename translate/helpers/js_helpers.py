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