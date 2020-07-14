import bashlex
import bash.code_to_gast.bash_helpers as bash_helpers

def node_to_gast(node):
   if type(node) == list:
      return node_to_gast(node[0])
   elif node.kind == 'command':
      return node_to_gast(node.parts)
   elif node.kind == 'word':
      return bash_helpers.word_to_gast(node)
