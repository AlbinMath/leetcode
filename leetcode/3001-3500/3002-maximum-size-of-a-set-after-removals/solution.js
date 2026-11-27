
var maximumSetSize = function(nums1, nums2) {
    const n = nums1.length;
    const limit = n / 2;

    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    const count1 = Math.min(limit, set1.size);
    const count2 = Math.min(limit, set2.size);
    const union = new Set([...set1, ...set2]).size;

    return Math.min(union, count1 + count2);
};

