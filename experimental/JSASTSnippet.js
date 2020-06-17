// Snippet for using AST to go from console.log() to print()
// NOTE: only works with single string arg for console.log()

const parser = require('@babel/parser').parse;

const inputCode = 'console.log("ss")';
let outputCode = "";

// parse the code -> ast
const ast = parser(inputCode, {sourceType: 'module'});

// loop through all expressions in body 
ast.program.body.forEach(handleExpression);

function handleExpression(expression) {

  // checks if function was called
  if (expression.type == 'ExpressionStatement' && expression.expression.type ==  "CallExpression") {
    // check if function was console.log
    if (expression.expression.callee.type == "MemberExpression") {
      // check object is console and property is log 
      const memberExpression = expression.expression.callee; 
      if (memberExpression.object.name == "console" && memberExpression.property.name == "log") {
        // console.log found - now need to handle args
        const args = expression.expression.arguments;
        // handle only default case string
        if (args[0].type == "StringLiteral" && args.length == 1) {
          const value = args[0].value;
          // TODO: how/when to handle writing out
          outputCode += "print(\"" + value + "\")\n";
        } 
      }
    }
  }
}
console.log("translated: " + outputCode);