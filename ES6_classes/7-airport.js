export default class Airport {
  constructor(name, code) {
    this.name = name;
    this.code = code;
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

  // Default string description returns airport code
  toString() {
    return `[object ${this._code}]`;
  }

  // Alternatively, using Symbol.toStringTag for modern JS
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
