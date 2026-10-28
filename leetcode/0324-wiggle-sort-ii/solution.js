/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    const arr = [...nums].sort((a, b) => a - b);
    const n = nums.length;
    let mid = Math.floor((n - 1) / 2);
    let end = n - 1;

    for (let i = 0; i < n; i++) {
        nums[i] = i % 2 === 0 ? arr[mid--] : arr[end--];
    }
};
