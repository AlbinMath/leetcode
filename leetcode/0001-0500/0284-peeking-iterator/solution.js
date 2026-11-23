/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {}
 * Iterator.prototype.next = function() {};
 * Iterator.prototype.hasNext = function() {};
 */

/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function(iterator) {
    this.iterator = iterator;
    this.hasPeeked = false;
    this.peekedValue = null;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function() {
    if (!this.hasPeeked) {
        this.peekedValue = this.iterator.next();
        this.hasPeeked = true;
    }
    return this.peekedValue;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function() {
    if (this.hasPeeked) {
        const value = this.peekedValue;
        this.hasPeeked = false;
        this.peekedValue = null;
        return value;
    }
    return this.iterator.next();
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function() {
    return this.hasPeeked || this.iterator.hasNext();
};
