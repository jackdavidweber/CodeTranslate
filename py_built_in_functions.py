import enum


class py_built_in_functions(enum.Enum):
    """
    All Python built in functions we support mapped to their corresponding 
    generic AST string
    """
    #Array manipulation
    append = "appendStatement"
    pop = "popStatement"
    sort = "sortStatement"
    extend = "extendStatement"
    reverse = "reverseStatement"

    #String manipulation
    find = "findStatement"
    split = "splitStatement"
    upper = "upperStatement"
    lower = "lowerStatement"
    index = "indexStatement"
    join = "joinStatement"

    #Dictionary manipulation
    keys = "keysStatement"
    values = "valuesStatement"
    update = "setStatement"
    clear = "clearStatement"
