const replace = require('iterable-transform-replace');
// replace `response` with `42`
const source = [1, 2, 'response', 3];
console.log(Array.from(replace('response', 42, source)));
