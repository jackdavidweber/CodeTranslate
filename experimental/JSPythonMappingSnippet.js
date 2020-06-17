/* 
* Code snippet for translating console.log to print
* using regular expressions and mapping between 
* languages. Only translates console.log statements
* ignores all other statements. 
*/

let userCode = "console.log(x);\n"; 
userCode += "   console.log(1 + 2);\n";
userCode += " 1 * 5;\n"
userCode += "console.log(\"simple string\");\n"
userCode += " console.log(\"hello\" + \"world\")"; 

// matches all console.log statements
const consoleLogPattern = /console\.log\((.*)\)/g;
// matches arguments in console.log statment 
const consoleLogArgPattern = /console\.log\((.*)\)/;

let outputCode = "";

// console.log instance found
if (consoleLogPattern.test(userCode)) {
  // returns all instances of console.log()
  const logStatments = userCode.match(consoleLogPattern);
  // for each console.log call write to output
  logStatments.forEach(logStatement =>
    // retrieve console -> print map here
    outputCode += "print(" + logStatement.match(consoleLogArgPattern)[1] + ")\n");
}

console.log(outputCode);