const bash_helpers = require('./bash_helpers.js')

function node_to_gast(node) {
    if (Array.isArray(node)) {
        return bash_helpers.array_to_gast(node)
    } else if (node["type"] === 'Script') {
        return bash_helpers.script_to_gast(node)
    } else if (node["type"] === 'Command') {
        return bash_helpers.command_to_gast(node)
    } else if (node["type"] === 'Word') {
        return bash_helpers.word_to_gast(node)
    }
}

exports.node_to_gast = node_to_gast

