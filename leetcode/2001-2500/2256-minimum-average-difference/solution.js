
var minimumAverageDifference = function(nums) {
    const n = nums.length;
    let totalSum = 0;
    for (let num of nums) {
        totalSum += num;
    }
    let leftSum = 0;
    let minDiff = Infinity;
    let answer = 0;
    for (let i = 0; i < n; i++) {
        leftSum += nums[i];
        let rightSum = totalSum - leftSum;
        let leftAvg = Math.floor(leftSum / (i + 1));
        let rightAvg = 0;
        if (i !== n - 1) {
            rightAvg = Math.floor(rightSum / (n - i - 1));
        }
        let diff = Math.abs(leftAvg - rightAvg);
        if (diff < minDiff) {
            minDiff = diff;
            answer = i;
        }
    }

    return answer;
};

