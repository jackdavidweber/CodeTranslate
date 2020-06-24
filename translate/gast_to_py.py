
generic_ast_to_python = {
    'logStatement': 'print', 
    'arrayPush' : 'append'
}

# Takes generic AST and returns Python source code
def gast_to_py(generic_ast):
  output_python = ''
  for statement in generic_ast['body']:
    if statement['type'] == 'logStatement':
      output_python += handle_log_statement(statement)
    elif statement['type'] == 'varAssign':  
      output_python += handle_var_assign(statement)
  #Get rid of last \n character
  return output_python[:-1]

def handle_log_statement(statement):
  output = generic_ast_to_python[statement['type']]
  output += '(\'' + statement['args'][0] + '\')\n'
  return output

def handle_var_assign(statement):
  output = ''
  if type(statement['varValue']) == str:
    output += statement['varId'] + ' = \'' + str(statement['varValue']) + '\'\n'
  else:
    output += statement['varId'] + ' = ' + str(statement['varValue']) + '\n'
  return output


ex = {
  "type": "root", 
  "body": [
    { 
      "type": "logStatement", 
      "args": ["Hello World!"]
    },
    {
      "type": "varAssign",
      "varId": "x",
      "varValue": 5
    }
  ]
}

print(gast_to_py(ex))

