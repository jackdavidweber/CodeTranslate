// Snippet for using AST to go from console.log() to print()
// NOTE: only works with single string arg for console.log()/

//const parser = require('@babel/parser').parse;
import babel from '@babel/core';
const inputCode = 'console.log("hello world")';
let outputCode = "";

// parse the code -> ast
const ast = babel.parse(inputCode)

// Approach using traverse for console.log() -> print()
babel.traverse(ast, {
  CallExpression: function(path) { 
    const args = (path.node.arguments);

    // function called on object
    if (path.node.callee.type == "MemberExpression") {
      const object = path.node.callee.object.name;
      const func = path.node.callee.property.name;
      // TODO: check if object.func is in map (console.log)
      outputCode += 'print("'
      // TODO: seperate functions to parse args 
      outputCode += args[0].value;
      outputCode += '")\n';
    }
    // function called
    if (path.node.callee.type == "Identifer") {
      const funcName = path.node.callee.name; 
    }
  }
});

// loop through all expressions in body 
//ast.program.body.forEach(handleExpression);

// Approach using if statements for console.log() -> print()
// Not ideal solution IMO
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