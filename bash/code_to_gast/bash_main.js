const bash_router = require("./bash_router.js")
const parse = require('bash-parser');

function bash_to_gast(bash_input) {
    let input_ast = ''
    try {
        input_ast = parse(bash_input);
    } catch(err) {
        return 'Error: code could not compile'
    }
    return bash_router.node_to_gast(input_ast)
}
