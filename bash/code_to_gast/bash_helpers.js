const bash_router = require("./bash_router.js")


function script_to_gast(node) {
    gast = {'type': 'root'}
    gast['body'] =  bash_router.node_to_gast(node['commands'])
    return gast
}

function array_to_gast(node) {
    let node_list = []
    for(const elem of node) {
        node_list.push(bash_router.node_to_gast(elem))
    }
    return node_list
}

function word_to_gast(node) {
    text = node['text']
    if (text === 'true') {
        return {'type': 'bool', 'value': 1}
    } else if (text === 'false') {
        return {'type': 'bool', 'value': 0}
    } else if (!isNaN(text)) {
        return {'type': 'num', 'value': Number(text)}
    } else {
        return {'type': 'str', 'value': text}
    }
        
}

exports.script_to_gast = script_to_gast
exports.array_to_gast = array_to_gast
exports.word_to_gast = word_to_gast