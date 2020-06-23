import sys
import os

# get path automatically and handle imports
path = os.path.dirname(os.getcwd()) + '/helpers'
sys.path.insert(1, path)
import steph_helpers

"""
Handles js var declerations to generic AST node
"""
def jsassign_to_gast(node):
  gast = {}
  gast["type"] = "varAssign"

  # only works with single assignment
  gast["varId"] = node[0].id.name
  gast["varValue"] = steph_helpers.jsarg_to_str(node[0].init)
  return gast