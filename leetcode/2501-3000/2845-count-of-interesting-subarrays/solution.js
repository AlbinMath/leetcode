
var countInterestingSubarrays = function(nums, modulo, k) {
    const freq = new Map();
    freq.set(0, 1);

    let prefix = 0;
    let ans = 0;

    for (let num of nums) {
        if (num % modulo === k) {
            prefix++;
        }

        let target = (prefix - k + modulo) % modulo;
        ans += freq.get(target) || 0;
        let remainder = prefix % modulo;

        freq.set(
            remainder,
            (freq.get(remainder) || 0) + 1
        );
    }

    return ans;
};

