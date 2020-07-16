const bash_helpers = require('./bash_helpers.js')
const bash_conditional = require('./bash_conditional.js')

/**
 * Recursive router that converts bash nodes to gast
 */
function node_to_gast(node) {
    if (Array.isArray(node)) {
        return bash_helpers.array_to_gast(node)
    } else if (node["type"] === 'Script') {
        return bash_helpers.script_to_gast(node)
    } else if (node["type"] === 'Command') {
        return bash_helpers.command_to_gast(node)
    } else if (node["type"] === 'Word') {
        return bash_helpers.word_to_gast(node)
    } else {
        return {"type": "error", "value": "unsupported"}
    }
}

exports.node_to_gast = node_to_gast

