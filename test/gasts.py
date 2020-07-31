gast_str = {"type": "str", "value": "hello world"}

gast_num = {"type": "num", "value": 47.47}

gast_true = {"type": "bool", "value": 1}

gast_false = {"type": "bool", "value": 0}

gast_arr = {
            "type":
                "arr",
            "elements": [{
                "type": "str",
                "value": "hello"
            }, {
                "type":
                    "arr",
                "elements": [{
                    "type": "num",
                    "value": 1
                }, {
                    "type": "num",
                    "value": 2
                }]
            }]
        }

gast_binOp_add = {
            'type': 'binOp',
            'op': '+',
            'left': {
                'type': 'num',
                'value': 3
            },
            'right': {
                'type': 'num',
                'value': 4
            }
        }

gast_binOp_bitwise = {
            'type': 'binOp',
            'op': '&',
            'left': {
                'type': 'num',
                'value': 1
            },
            'right': {
                'type': 'num',
                'value': 3
            }
        }

gast_binOp_add_sub_mult_div = {
            'type': 'binOp',
            'op': '-',
            'left': {
                'type': 'binOp',
                'op': '+',
                'left': {
                    'type': 'num',
                    'value': 1
                },
                'right': {
                    'type': 'num',
                    'value': 2
                }
            },
            'right': {
                'type': 'binOp',
                'op': '/',
                'left': {
                    'type': 'binOp',
                    'op': '*',
                    'left': {
                        'type': 'num',
                        'value': 3
                    },
                    'right': {
                        'type': 'num',
                        'value': 4
                    }
                },
                'right': {
                    'type': 'num',
                    'value': 5
                }
            }
        }

gast_boolOp_and = {
            'type': 'boolOp',
            'op': '&&',
            'left': {
                'type': 'bool',
                'value': 1
            },
            'right': {
                'type': 'bool',
                'value': 0
            }
        }

gast_boolOp_or_and = {
            'type': 'boolOp',
            'op': '||',
            'left': {
                'type': 'bool',
                'value': 1
            },
            'right': {
                'type': 'boolOp',
                'op': '&&',
                'left': {
                    'type': 'bool',
                    'value': 0
                },
                'right': {
                    'type': 'num',
                    'value': 4
                }
            }
        }

gast_logStatement_bool = {
            "type":
                "root",
            "body": [{
                "type": "funcCall",
                "args": [{
                    "type": "bool",
                    "value": 0
                }],
                "value": {
                    "type": "logStatement"
                }
            }]
        }

gast_logStatement_two_args = {
            "type":
                "root",
            "body": [{
                "type": "funcCall",
                "args": [{
                    "type": "str",
                    "value": "hello world"
                }, {
                    "type": "num",
                    "value": 5
                }],
                "value": {
                    "type": "logStatement"
                }
            }]
        }

gast_varAssign_let = {
            "type":
                "root",
            "body": [{
                "type": "varAssign",
                "kind": "let",
                "varId": {
                    "type": "name",
                    "value": "x"
                },
                "varValue": {
                    "type": "num",
                    "value": 5
                }
            },]
        }

gast_varAssign_const = {
            "type":
                "root",
            "body": [{
                "type": "varAssign",
                "kind": "const",
                "varId": {
                    "type": "name",
                    "value": "x"
                },
                "varValue": {
                    "type": "num",
                    "value": 5
                }
            },]
        }

gast_multi_body = {
            "type":
                "root",
            "body": [
                {
                    "type": "varAssign",
                    "kind": "const",
                    "varId": {
                        "type": "name",
                        "value": "x"
                    },
                    "varValue": {
                        "type": "num",
                        "value": 5
                    }
                },
                {
                    "type": "varAssign",
                    "kind": "const",
                    "varId": {
                        "type": "name",
                        "value": "x"
                    },
                    "varValue": {
                        "type": "num",
                        "value": 5
                    }
                },
            ]
        }

gast_if_log = {
            'type':
                'root',
            'body': [{
                'type': 'if',
                'body': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': 'This is true'
                    }]
                }],
                'orelse': [],
                'test': {
                    'type': 'bool',
                    'value': 1
                }
            }]
        }

gast_else_log = {
            'type':
                'root',
            'body': [{
                'type': 'if',
                'body': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': '1 is true'
                    }]
                }],
                'orelse': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': '1 is NOT true'
                    }]
                }],
                'test': {
                    'type': 'num',
                    'value': 1
                }
            }]
        }

gast_elif_log = {
            'type':
                'root',
            'body': [{
                'type': 'if',
                'body': [{
                    'type': 'funcCall',
                    'value': {
                        'type': 'logStatement'
                    },
                    'args': [{
                        'type': 'str',
                        'value': '1 is true'
                    }]
                }],
                'orelse': [{
                    'type': 'if',
                    'body': [{
                        'type': 'funcCall',
                        'value': {
                            'type': 'logStatement'
                        },
                        'args': [{
                            'type': 'str',
                            'value': '2 is true'
                        }]
                    }, {
                        'type': 'funcCall',
                        'value': {
                            'type': 'logStatement'
                        },
                        'args': [{
                            'type': 'str',
                            'value': 'second line'
                        }]
                    }],
                    'orelse': [],
                    'test': {
                        'type': 'num',
                        'value': 2
                    }
                }],
                'test': {
                    'type': 'num',
                    'value': 1
                }
            }]
        }

gast_for_range = {
            "type": "forRangeStatement",
            "init": {
                "type": "varAssign",
                "kind": "let",
                "varId": {
                    "type": "name",
                    "value": "i"
                },
                "varValue": {
                    "type": "num",
                    "value": 0
                }
            },
            "test": {
                "type": "binOp",
                "left": {
                    "type": "name",
                    "value": "i"
                },
                "op": "<",
                "right": {
                    "type": "num",
                    "value": 10
                }
            },
            "update": {
                "type": "augAssign",
                "left": {
                    "type": "name",
                    "value": "i"
                },
                "op": "+=",
                "right": {
                    "type": "num",
                    "value": 2
                }
            },
            "body": [{
                "type": "num",
                "value": 5
            }]
        }

gast_for_of = {
            "type": "forOfStatement",
            "init": {
                "type": "name",
                "value": "elem"
            },
            "iter": {
                "type":
                    "arr",
                "elements": [{
                    "type": "num",
                    "value": 1
                }, {
                    "type": "num",
                    "value": 2
                }]
            },
            "body": [{
                "type": "num",
                "value": 5
            }]
        }

gast_indent_if = {
            'type':
                'root',
            'body': [{
                'type': 'if',
                'body': [{
                    'type': 'if',
                    'body': [{
                        'type': 'funcCall',
                        'value': {
                            'type': 'logStatement'
                        },
                        'args': [{
                            'type': 'str',
                            'value': 'y and x are true'
                        }]
                    }],
                    'orelse': [],
                    'test': {
                        'type': 'binOp',
                        'left': {
                            'type': 'name',
                            'value': 'y'
                        },
                        'op': '==',
                        'right': {
                            'type': 'bool',
                            'value': 1
                        }
                    }
                }],
                'orelse': [],
                'test': {
                    'type': 'binOp',
                    'left': {
                        'type': 'name',
                        'value': 'x'
                    },
                    'op': '==',
                    'right': {
                        'type': 'bool',
                        'value': 1
                    }
                }
            }]
        }

gast_indent_for_of = {
            'type':
                'root',
            'body': [{
                'type':
                    'forOfStatement',
                'init': {
                    'type': 'name',
                    'value': 'j'
                },
                'iter': {
                    'type':
                        'arr',
                    'elements': [{
                        'type': 'num',
                        'value': 1
                    }, {
                        'type': 'num',
                        'value': 2
                    }]
                },
                'body': [{
                    'type':
                        'forOfStatement',
                    'init': {
                        'type': 'name',
                        'value': 'k'
                    },
                    'iter': {
                        'type':
                            'arr',
                        'elements': [{
                            'type': 'num',
                            'value': 3
                        }, {
                            'type': 'num',
                            'value': 4
                        }]
                    },
                    'body': [{
                        'type': 'name',
                        'value': 'j'
                    }, {
                        'type': 'name',
                        'value': 'k'
                    }]
                }]
            }]
        }