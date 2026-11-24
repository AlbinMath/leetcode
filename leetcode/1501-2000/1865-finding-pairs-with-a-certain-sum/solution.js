
var FindSumPairs = function(nums1, nums2) {
    this.nums1 = nums1;
    this.nums2 = nums2;
    this.freq2 = new Map();
    
    for (const num of nums2) {
        this.freq2.set(num, (this.freq2.get(num) || 0) + 1);
    }
};
FindSumPairs.prototype.add = function(index, val) {
    const oldVal = this.nums2[index];
    this.freq2.set(oldVal, this.freq2.get(oldVal) - 1);
    
    const newVal = oldVal + val;
    this.nums2[index] = newVal;
    this.freq2.set(newVal, (this.freq2.get(newVal) || 0) + 1);
};

FindSumPairs.prototype.count = function(tot) {
    let pairs = 0;
    for (const x of this.nums1) {
        pairs += this.freq2.get(tot - x) || 0;
    }
    return pairs;
};
