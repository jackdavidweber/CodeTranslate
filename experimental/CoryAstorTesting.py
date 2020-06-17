import astor
import ast

# Useful commands:
# astor.dump_tree(node) - prints pretty version of AST tree

#Parse code using astor
node = astor.code_to_ast.parse_file('ExamplePythonFile.py')
body = node.body
output = ''

#Pretty print the AST
print(astor.dump_tree(node))

for elem in body:
  #Handle elements of type Expression
  if type(elem) == ast.Expr:
    if type(elem.value) == ast.Call:
      function = elem.value.func
      if type(function) == ast.Name:
        arguments = elem.value.args
        #Check only one argument and that it's a string
        if len(arguments) == 1 and type(arguments[0]) == ast.Str:
            output += 'console.log(\'' + arguments[0].s + '\')'

print(output)
    