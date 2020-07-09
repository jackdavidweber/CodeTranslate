import enum

"""
All Python built in functions we support mapped to their corresponding 
generic AST string
"""
class py_built_in_functions(enum.Enum):
    append = "appendStatement"
    pop = "popStatement"
    sort = "sortStatement"
    extend = "extendStatement"