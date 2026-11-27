
var maxKDistinct = function(nums, k) {
    const unique = [...new Set(nums)];

    unique.sort((a, b) => b - a);

    return unique.slice(0, k);
};

