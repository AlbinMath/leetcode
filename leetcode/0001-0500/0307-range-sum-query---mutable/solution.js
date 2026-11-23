
var NumArray = function(nums) {
    this.n = nums.length;
    this.tree = new Array(2 * this.n).fill(0);

    // Build the segment tree
    for (let i = 0; i < this.n; i++) {
        this.tree[this.n + i] = nums[i];
    }

    for (let i = this.n - 1; i > 0; i--) {
        this.tree[i] = this.tree[2 * i] + this.tree[2 * i + 1];
    }
};

NumArray.prototype.update = function(index, val) {
    let pos = index + this.n;

    // Update the leaf node
    this.tree[pos] = val;

    // Update all parent nodes
    while (pos > 1) {
        pos = Math.floor(pos / 2);
        this.tree[pos] = this.tree[2 * pos] + this.tree[2 * pos + 1];
    }
};

NumArray.prototype.sumRange = function(left, right) {
    let sum = 0;

    left += this.n;
    right += this.n;

    // Query the inclusive range [left, right]
    while (left <= right) {
        if (left % 2 === 1) {
            sum += this.tree[left];
            left++;
        }

        if (right % 2 === 0) {
            sum += this.tree[right];
            right--;
        }

        left = Math.floor(left / 2);
        right = Math.floor(right / 2);
    }

    return sum;
};

