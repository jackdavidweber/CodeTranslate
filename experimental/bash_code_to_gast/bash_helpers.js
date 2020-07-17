const bash_router = require("./bash_router.js")

/**
 * Handles the script type which is the top level node that every command has
 */
function script_to_gast(node) {
    gast = {"type": "root"}
    gast["body"] =  bash_router.node_to_gast(node["commands"])
    return gast
}

/**
 * Handles an array object and converting to gast
 */
function array_to_gast(node) {
    let node_list = []
    for(const elem of node) {
        node_list.push(bash_router.node_to_gast(elem))
    }
    return node_list
}

/**
 * Word nodes are base cases such as strings and numbers
 */ 
function word_to_gast(node) {
    text = node["text"]
    if (text === "true") {
        return {"type": "bool", "value": 1}
    } else if (text === "false") {
        return {"type": "bool", "value": 0}
    } else if (!isNaN(text)) {
        //Checks if it can be parsed into a number
        return {"type": "num", "value": Number(text)}
    } else {
        return {"type": "str", "value": text}
    }
}

/**
 * Converts command nodes such as function calls to gast
 */
function command_to_gast(node) {
    // TODO update to handle more than just echo function
    if ("suffix" in node) { 
        gast = {"type": "funcCall"}
        gast["args"] = bash_router.node_to_gast(node["suffix"])
        gast["value"] = {"type": "logStatement"}
        return gast
    } else {
        return bash_router.node_to_gast(node["name"])
    }
}

//Export all functions in the file
exports.script_to_gast = script_to_gast
exports.array_to_gast = array_to_gast
exports.word_to_gast = word_to_gast
exports.command_to_gast = command_to_gast