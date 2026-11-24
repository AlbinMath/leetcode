/**
 * @param {number[]} encoding
 */
var RLEIterator = function(encoding) {
    this.encoding = encoding;
    this.index = 0;
};

/**
 * @param {number} n
 * @return {number}
 */
RLEIterator.prototype.next = function(n) {
    while (this.index < this.encoding.length) {
        if (this.encoding[this.index] >= n) {
            this.encoding[this.index] -= n;
            return this.encoding[this.index + 1];
        }

        n -= this.encoding[this.index];
        this.index += 2;
    }

    return -1;
};
