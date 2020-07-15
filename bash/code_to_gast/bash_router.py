import bashlex
import bash.code_to_gast.bash_helpers as bash_helpers

def node_to_gast(node):
   if type(node) == list:
      node_list = []
      for part in node:
         node_list.append(node_to_gast(part))
      return node_list
   elif node.kind == 'command':
      return node_to_gast(node.parts)
   elif node.kind == 'word':
      return bash_helpers.word_to_gast(node)
