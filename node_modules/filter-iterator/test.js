'use strict'

let expect = require('expect.js');
let nats = require('naturals');
let filter = require('./');

function even(x) {
  return x % 2 === 0;
}

describe('filter-iterator', function(){
  it('works', function(){
    let xs = filter(nats(), even)

    expect(xs.next().value).to.be(0)
    expect(xs.next().value).to.be(2)
    expect(xs.next().value).to.be(4)
  });
});
