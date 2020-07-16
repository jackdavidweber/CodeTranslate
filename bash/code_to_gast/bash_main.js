const bash_router = require("./bash_router.js")
const parse = require("bash-parser");

const bash_input = "if 1 == 1 ; then\necho 8\nfi"//process.argv[2]
let input_ast = ""
try {
    input_ast = parse(bash_input);
} catch(err) {
    return "Error: code could not compile"
}

console.log(JSON.stringify(bash_router.node_to_gast(input_ast)))