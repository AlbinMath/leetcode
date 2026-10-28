/**
 * @param {number} k
 */
var MyCircularQueue = function (k) {
    this.data = new Array(k);
    this.cap = k;
    this.head = 0;
    this.size = 0;
};

/**
 * @param {number} value
 * @return {boolean}
 */
MyCircularQueue.prototype.enQueue = function (value) {
    if (this.isFull()) return false;
    this.data[(this.head + this.size) % this.cap] = value;
    this.size++;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.deQueue = function () {
    if (this.isEmpty()) return false;
    this.head = (this.head + 1) % this.cap;
    this.size--;
    return true;
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Front = function () {
    return this.isEmpty() ? -1 : this.data[this.head];
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Rear = function () {
    return this.isEmpty() ? -1 : this.data[(this.head + this.size - 1) % this.cap];
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isEmpty = function () {
    return this.size === 0;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isFull = function () {
    return this.size === this.cap;
};
