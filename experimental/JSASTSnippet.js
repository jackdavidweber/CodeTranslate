// Snippet for using AST to go from console.log() to print()
// NOTE: only works with single string arg for console.log()/

//const parser = require('@babel/parser').parse;
import babel from '@babel/core';
//const inputCode = 'console.log("hello world")\n console.log(2)\n console.log("helloo", "world")';
const inputCode = 'let x  = "sa"\n const y = 2;\n console.log("hello world")';

// parse the code -> ast
const ast = babel.parse(inputCode)

let genericAst = {
	"type": "root",
	"body": []
}


// Approach using traverse for console.log() -> print()
babel.traverse(ast, {
  CallExpression: function(path) { 
    // function called on object
    if (path.node.callee.type == "MemberExpression") {
      const object = path.node.callee.object.name;
      const func = path.node.callee.property.name;

      if (object == "console" && func == "log") {
        let args = [];
        for (const arg of path.node.arguments) {
          // handles printing variables
          if (arg.type == "Identifier") {
            args.push(arg.name);
          } else {
            args.push(arg.extra.raw);
          }
        }
        genericAst.body.push({"type": "logStatement", "args" : args});
      }
    }
    
    // function called
    if (path.node.callee.type == "Identifer") {
      const funcName = path.node.callee.name; 
    }
  },

  // handles var declerations
  // current supports only numbers and strings 
  VariableDeclaration(path) {
    // TODO: handle multiple declarations
    const name = path.node.declarations[0].id.name;
    const val = path.node.declarations[0].init.extra.raw;
    genericAst.body.push({"type": "varAssign", "varId" : name, "varValue" : val});
  }

});

console.log(genericAst);

// read from generic AST
for (const statement of genericAst.body) {
  // translate logStatement to Python
  if (statement.type == "logStatement") {
    let translation = "print(";
    for (const arg of statement.args) {
      // NOTE: console.log("Hello", "world") -> print("Hello""world")
      // TODO: fix when multiple args given
      translation += arg;
    }
    translation += ")";
    console.log(translation);
  }

  // varr declaratioon
  if (statement.type == "varAssign") {
    console.log(statement.varId += " = " + statement.varValue);
  }
}


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
