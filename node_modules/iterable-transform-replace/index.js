'use strict';

function _interopDefault (ex) { return (ex && (typeof ex === 'object') && 'default' in ex) ? ex['default'] : ex; }

var curry = _interopDefault(require('curry'));

function replace(oldItem, newItem, array) {
	return array.map(item => {
		if (item === oldItem) {
			return newItem;
		}

		return item;
	});
}

var main = curry(replace);

module.exports = main;
