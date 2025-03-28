export default class Currency {
	constructor(code, name) {
	  this.code = code;  // Uses the setter
	  this.name = name;  // Uses the setter
	}
  
	// Code getter and setter
	get code() {
	  return this._code;
	}
  
	set code(value) {
	  if (typeof value !== 'string') {
		throw new TypeError('Code must be a string');
	  }
	  this._code = value;
	}
  
	// Name getter and setter
	get name() {
	  return this._name;
	}
  
	set name(value) {
	  if (typeof value !== 'string') {
		throw new TypeError('Name must be a string');
	  }
	  this._name = value;
	}
  
	// Method to display full currency format
	displayFullCurrency() {
	  return `${this._name} (${this._code})`;
	}
  }
  