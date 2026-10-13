
var findNumberOfLIS = function(nums) {
    const n = nums.length;

    const length = new Array(n).fill(1);
    const count = new Array(n).fill(1);

    let maxLength = 1;
    let result = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (length[j] + 1 > length[i]) {
                    length[i] = length[j] + 1;
                    count[i] = count[j];
                } else if (length[j] + 1 === length[i]) {
                    count[i] += count[j];
                }
            }
        }

        maxLength = Math.max(maxLength, length[i]);
    }

    for (let i = 0; i < n; i++) {
        if (length[i] === maxLength) {
            result += count[i];
        }
    }

    return result;
};

