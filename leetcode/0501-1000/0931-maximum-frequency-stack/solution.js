
var FreqStack = function() {
    this.freq = new Map();
    this.group = new Map();
    this.maxFreq = 0;
};

/**
 * @param {number} val
 * @return {void}
 */
FreqStack.prototype.push = function(val) {
    // Increase frequency
    const f = (this.freq.get(val) || 0) + 1;
    this.freq.set(val, f);

    // Update maximum frequency
    this.maxFreq = Math.max(this.maxFreq, f);

    // Create frequency group if needed
    if (!this.group.has(f)) {
        this.group.set(f, []);
    }

    // Add value to its frequency group
    this.group.get(f).push(val);
};

/**
 * @return {number}
 */
FreqStack.prototype.pop = function() {
    // Get the most recent element with maximum frequency
    const stack = this.group.get(this.maxFreq);
    const val = stack.pop();

    // Decrease frequency
    this.freq.set(val, this.freq.get(val) - 1);

    // If group is empty, reduce maximum frequency
    if (stack.length === 0) {
        this.maxFreq--;
    }

    return val;
};

