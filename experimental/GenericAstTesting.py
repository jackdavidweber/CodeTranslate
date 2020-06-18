import astor
import ast
import json


def pythonToAst(filename):
  pythonToGenericAst = {'print':'logStatement'}
  srcAst = astor.code_to_ast.parse_file(filename)
  body = srcAst.body
  print(astor.dump_tree(srcAst))

  convertedAst = {'type': 'root', 'body': []}
  for statement in body:
    if type(statement) == ast.Expr:
      convertedAst['body'].append(handleExpression(statement, pythonToGenericAst))
  
  print(convertedAst)

def handleExpression(statement, pythonToGenericAst):
  if type(statement.value) == ast.Call:
    func = statement.value.func
    args = statement.value.args[0]
    if type(func) == ast.Name:
      return {'type': pythonToGenericAst[func.id], 'args': [args.s]}


def astToPython(genericAst):
  genericAstToPython = {'logStatement': 'print'}
  outputPython = ''
  for statement in genericAst['body']:
    outputPython += genericAstToPython[statement['type']]
    outputPython += '(\'' + statement['args'][0] + '\')'
  print(outputPython)


pythonToAst('ExamplePythonFile.py')

json = json.load(open('ExampleJson.json'))
astToPython(json)