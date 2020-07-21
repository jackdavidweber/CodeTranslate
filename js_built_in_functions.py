import enum
"""
All JavaScript built in functions we support mapped to their corresponding 
generic AST string
"""


class js_built_in_functions(enum.Enum):
    #Array manipulation
    push = "appendStatement"
    pop = "popStatement"
    sort = "sortStatement"
    concat = "extendStatement"
    reverse = "reverseStatement"

    #String manipulation
    search = "findStatement"
    split = "splitStatement"
    toUpperCase = "upperStatement"
    toLowerCase = "lowerStatement"
    indexOf = "indexStatement"
    join = "joinStatement"

    #Dictionary manipulation
    keys = "keysStatement"
    values = "valuesStatement"
    set = "setStatement"
    clear = "clearStatement"
