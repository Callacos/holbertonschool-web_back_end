export default class Building {
	constructor(sqft) {
	  if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
		throw new Error('Class extending Building must override evacuationWarningMessage');
	  }
	  this.sqft = sqft;
	}
  
	// sqft getter
	get sqft() {
	  return this._sqft;
	}
  
	// sqft setter with type validation
	set sqft(value) {
	  if (typeof value !== 'number') {
		throw new TypeError('sqft must be a number');
	  }
	  this._sqft = value;
	}
  }
  