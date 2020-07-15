var assert = require('assert')
var hasOwnProperty = require('./')

var obj = { a: 1, c: 2 }

assert.equal(hasOwnProperty(obj, 'a'), true)
assert.equal(hasOwnProperty(obj, 'b'), false)
assert.equal(hasOwnProperty(obj, 'c'), true)

assert.equal(hasOwnProperty(obj, 'toString'), false)
assert.equal(hasOwnProperty(obj, 'valueOf'), false)
