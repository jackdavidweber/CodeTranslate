
def word_to_gast(node):
    literal = node.word
    if literal == 'true':
        return {'type': 'bool', 'value': 1}
    elif literal == 'false':
        return {'type': 'bool', 'value': 0}
    else:
        try:
            int(literal)
            return {'type': 'num', 'value': int(literal)}
        except ValueError:
            try:
                float(literal)
                return {'type': 'num', 'value': float(literal)}
            except:
                return {'type': 'str', 'value': literal}