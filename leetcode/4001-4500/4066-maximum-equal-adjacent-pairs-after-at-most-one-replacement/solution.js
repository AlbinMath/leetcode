
var maxEqualAdjacentPairs = function(nums) {
    let map = new Map();
    let ans = 0;
    let maxCount = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        let x = nums[i];
        let y = nums[i + 1];

        if (x === y) {
            ans++;
        } else {
            let key = `${Math.min(x, y)},${Math.max(x, y)}`;

            let freq = (map.get(key) || 0) + 1;
            map.set(key, freq);

            maxCount = Math.max(maxCount, freq);
        }
    }

    return ans + maxCount;
};

