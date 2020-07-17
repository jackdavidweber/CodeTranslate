const bash_router = require("./bash_router.js")

/**
 * Handles the script type which is the top level node that every command has
 */
function script_to_gast(node) {
    const gast = {"type": "root"}
    gast["body"] =  bash_router.node_to_gast(node["commands"])
    return gast
}

/**
 * Handles an array object and converting to gast
 */
function array_to_gast(node) {
    const node_list = []
    for(const elem of node) {
        node_list.push(bash_router.node_to_gast(elem))
    }
    return node_list
}

/**
 * Word nodes are base cases such as strings and numbers
 */ 
function word_to_gast(node) {
    const text = node["text"]
    if (isNaN(text)) {
        return {"type": "str", "value": text}
    } else {
        return {"type": "num", "value": Number(text)}
    }
}

/**
 * Converts command nodes such as function calls to gast
 */
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

/**
* Converts compound lists to gast nodes
*/
function compound_list_to_gast(node) {
    return bash_router.node_to_gast(node["commands"])
}

//Export all functions in the file
exports.script_to_gast = script_to_gast
exports.array_to_gast = array_to_gast
exports.word_to_gast = word_to_gast
exports.command_to_gast = command_to_gast
exports.compound_list_to_gast = compound_list_to_gast