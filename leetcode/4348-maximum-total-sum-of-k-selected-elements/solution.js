
var maxSum = function(nums, k, mul) {
    nums.sort((a, b) => b - a);

    let answer = 0;

    for (let i = 0; i < k; i++) {
        const multiplier = Math.max(1, mul - i);
        answer += nums[i] * multiplier;
    }

    return answer;
};

