const bash_router = require('./bash_router.js')

function if_to_gast(node) {
    const gast = {"type": "if", "orelse": []}
    gast["body"] = bash_router.node_to_gast(node["then"])
    gast["test"] = bash_router.node_to_gast(node["clause"])
    return gast
}

exports.if_to_gast = if_to_gast