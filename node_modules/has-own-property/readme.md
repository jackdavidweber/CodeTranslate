# Has Own Property?

Check if an object has a local property.

## Installation

```sh
npm install --save has-own-property
```

## Usage

```js
const hasOwnProperty = require('has-own-property')

const obj = { a: 1 }

hasOwnProperty(obj, 'a') // true
hasOwnProperty(obj, 'b') // false
```
