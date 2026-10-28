/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation.
 * function NestedInteger() {}
 * NestedInteger.prototype.isInteger = function() {};
 * NestedInteger.prototype.getInteger = function() {};
 * NestedInteger.prototype.getList = function() {};
 */

/**
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {
    this.stack = nestedList.slice().reverse();
};

/**
 * @return {number}
 */
NestedIterator.prototype.next = function() {
    this.hasNext();
    return this.stack.pop().getInteger();
};

/**
 * @return {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    while (this.stack.length > 0) {
        const top = this.stack[this.stack.length - 1];

        if (top.isInteger()) {
            return true;
        }

        this.stack.pop();
        const list = top.getList();

        for (let i = list.length - 1; i >= 0; i--) {
            this.stack.push(list[i]);
        }
    }

    return false;
};
