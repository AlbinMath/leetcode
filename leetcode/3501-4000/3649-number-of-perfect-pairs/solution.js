
var perfectPairs = function(nums) {
    const arr = nums.map(Math.abs).sort((a, b) => a - b);

    let count = 0;
    let left = 0;
    for (let right = 0; right < arr.length; right++) {
        while (arr[right] > 2 * arr[left]) {
            left++;
        }
        count += right - left;
    }

    return count;
};

