/**
 * @param {number} k
 */
var MyCircularDeque = function (k) {
    this.data = new Array(k);
    this.cap = k;
    this.head = 0;
    this.size = 0;
};

/**
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function (value) {
    if (this.isFull()) return false;
    this.head = (this.head - 1 + this.cap) % this.cap;
    this.data[this.head] = value;
    this.size++;
    return true;
};

/**
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function (value) {
    if (this.isFull()) return false;
    this.data[(this.head + this.size) % this.cap] = value;
    this.size++;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function () {
    if (this.isEmpty()) return false;
    this.head = (this.head + 1) % this.cap;
    this.size--;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function () {
    if (this.isEmpty()) return false;
    this.size--;
    return true;
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function () {
    return this.isEmpty() ? -1 : this.data[this.head];
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function () {
    return this.isEmpty() ? -1 : this.data[(this.head + this.size - 1) % this.cap];
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function () {
    return this.size === 0;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function () {
    return this.size === this.cap;
};
