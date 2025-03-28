export default class Car {
	constructor(brand, motor, color) {
	  this.brand = brand;
	  this.motor = motor;
	  this.color = color;
	}
  
	// Brand getter and setter
	get brand() {
	  return this._brand;
	}
  
	set brand(value) {
	  if (typeof value !== 'string') {
		throw new TypeError('Brand must be a string');
	  }
	  this._brand = value;
	}
  
	// Motor getter and setter
	get motor() {
	  return this._motor;
	}
  
	set motor(value) {
	  if (typeof value !== 'string') {
		throw new TypeError('Motor must be a string');
	  }
	  this._motor = value;
	}
  
	// Color getter and setter
	get color() {
	  return this._color;
	}
  
	set color(value) {
	  if (typeof value !== 'string') {
		throw new TypeError('Color must be a string');
	  }
	  this._color = value;
	}
  
	// Clone method using structuredClone for deep copy
	cloneCar() {
	  return structuredClone(this);
	}
  }
  