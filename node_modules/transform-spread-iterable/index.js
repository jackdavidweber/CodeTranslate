'use strict';

function * spread(source) {
	for (const item of source) {
		if (typeof item[Symbol.iterator] === 'function') {
			yield * item;
		} else {
			yield item;
		}
	}
}

module.exports = spread;
