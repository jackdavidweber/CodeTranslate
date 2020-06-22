import plyj.parser as plyj

input_code = 'System.out.println()'
parser = plyj.Parser()

tree = parser.parse_expression(input_code)
print(tree)

file_tree = parser.parse_file('ExampleJavaCode.java')
print(file_tree)