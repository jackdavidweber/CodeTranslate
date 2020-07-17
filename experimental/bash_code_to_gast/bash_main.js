const bash_router = require("./bash_router.js")
const parse = require("bash-parser");

const bash_input = process.argv[2]
let input_ast = ""
try {
    input_ast = parse(bash_input);
} catch(err) {
    return "Error: code could not compile"
}

const gast = bash_router.node_to_gast(input_ast)
const json_string = JSON.stringify(gast)
console.log(json_string)
