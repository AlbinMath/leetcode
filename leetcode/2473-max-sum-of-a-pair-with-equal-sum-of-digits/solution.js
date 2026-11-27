
var maximumSum = function(nums) {
    const map = new Map();
    let maxSum = -1;
    const digitSum = (num) => {
        let sum = 0;

        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }

        return sum;
    };

    for (const num of nums) {
        const sum = digitSum(num);

        if (map.has(sum)) {
            maxSum = Math.max(maxSum, num + map.get(sum));

            map.set(sum, Math.max(num, map.get(sum)));
        } else {
            map.set(sum, num);
        }
    }

    return maxSum;
};

