# object-pairs [![Build Status][travis-badge]][travis] [![Dependency Status][david-badge]][david]

[![npm](https://nodei.co/npm/object-pairs.png)](https://nodei.co/npm/object-pairs/)

[travis]: https://travis-ci.org/eush77/object-pairs
[travis-badge]: https://travis-ci.org/eush77/object-pairs.svg
[david]: https://david-dm.org/eush77/object-pairs
[david-badge]: https://david-dm.org/eush77/object-pairs.png

Turn an object into list of `[key, value]` pairs for mapping, iterating or other purposes.

## Example

```js
> pairs = require('object-pairs')
[Function]
> pairs({ foo: 2, bar: 4 })
[ [ 'foo', 2 ],
  [ 'bar', 4 ] ]
```

## API

### `pairs(obj)`

Return list of key-value pairs.

## Install

```shell
npm install object-pairs
```

## License

MIT
