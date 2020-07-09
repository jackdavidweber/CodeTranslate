import enum

"""
All JavaScript built in functions we support mapped to their corresponding 
generic AST string
"""
class js_built_in_functions(enum.Enum):
    push = "appendStatement"
    pop = "popStatement"
    sort = "sortStatement"
    concat = "extendStatement"