var constructTransformedArray = function(nums) {
    const n = nums.length;
    return nums.map((num, i) => nums[(((i + num) % n) + n) % n]);
};
