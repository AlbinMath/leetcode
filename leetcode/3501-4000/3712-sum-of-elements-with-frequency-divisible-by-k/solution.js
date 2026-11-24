
var sumDivisibleByK = function(nums, k) {
    let freq = new Array(101).fill(0);

    // Count frequency
    for (let num of nums) {
        freq[num]++;
    }

    let sum = 0;

    // Check frequency divisible by k
    for (let i = 1; i <= 100; i++) {
        if (freq[i] > 0 && freq[i] % k === 0) {
            sum += i * freq[i];
        }
    }

    return sum;
};

