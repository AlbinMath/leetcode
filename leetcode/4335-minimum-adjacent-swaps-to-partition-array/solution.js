
var minAdjacentSwaps = function(nums, a, b) {
    const MOD = 1000000007;

    let count1 = 0;
    let count2 = 0;
    let answer = 0;

    for (const num of nums) {
        if (num < a) {
            answer = (answer + count1 + count2) % MOD;
        } else if (num <= b) {
            answer = (answer + count2) % MOD;
            count1++;
        } else {
            count2++;
        }
    }

    return answer;
};

