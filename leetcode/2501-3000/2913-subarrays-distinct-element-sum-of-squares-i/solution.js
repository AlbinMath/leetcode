
var sumCounts = function(nums) {
    let result = 0;

    for (let i = 0; i < nums.length; i++) {
        const distinct = new Set();

        for (let j = i; j < nums.length; j++) {
            distinct.add(nums[j]);

            const count = distinct.size;
            result += count * count;
        }
    }

    return result;
};

