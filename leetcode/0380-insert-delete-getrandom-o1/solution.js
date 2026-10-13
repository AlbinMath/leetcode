
var RandomizedSet = function() {
    this.nums = [];
    this.indices = new Map();
};

RandomizedSet.prototype.insert = function(val) {
    if (this.indices.has(val)) {
        return false;
    }

    this.indices.set(val, this.nums.length);
    this.nums.push(val);

    return true;
};

RandomizedSet.prototype.remove = function(val) {
    if (!this.indices.has(val)) {
        return false;
    }

    const index = this.indices.get(val);
    const lastVal = this.nums[this.nums.length - 1];

    this.nums[index] = lastVal;
    this.indices.set(lastVal, index);

    this.nums.pop();
    this.indices.delete(val);

    return true;
};

RandomizedSet.prototype.getRandom = function() {
    const randomIndex = Math.floor(Math.random() * this.nums.length);
    return this.nums[randomIndex];
};

