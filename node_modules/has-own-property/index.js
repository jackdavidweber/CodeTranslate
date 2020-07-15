var _hasOwnProperty = Object.prototype.hasOwnProperty

module.exports = function hasOwnProperty (obj, prop) {
  return _hasOwnProperty.call(obj, prop)
}
