const bash_router = require("./bash_router.js")


function script_to_gast(node) {
    const gast = {"type": "root"}
    gast["body"] =  bash_router.node_to_gast(node["commands"])
    return gast
}

function array_to_gast(node) {
    const node_list = []
    for(const elem of node) {
        node_list.push(bash_router.node_to_gast(elem))
    }
    return node_list
}

function word_to_gast(node) {
    const text = node["text"]
    if (!isNaN(text)) {
        return {"type": "num", "value": Number(text)}
    } else {
        return {"type": "str", "value": text}
    }
}

function command_to_gast(node) {
    // TODO update to handle more than just echo function
    if ("suffix" in node) { 
        const gast = {"type": "funcCall"}
        gast["args"] = bash_router.node_to_gast(node["suffix"])
        gast["value"] = {"type": "logStatement"}
        return gast
    } else {
        return bash_router.node_to_gast(node["name"])
    }
}

function compound_list_to_gast(node) {
    return bash_router.node_to_gast(node["commands"])
}

exports.script_to_gast = script_to_gast
exports.array_to_gast = array_to_gast
exports.word_to_gast = word_to_gast
exports.command_to_gast = command_to_gast
exports.compound_list_to_gast = compound_list_to_gast