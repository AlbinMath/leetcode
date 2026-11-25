
var maximumSubarraySum = function(nums, k) {
    const map = new Map();
    let prefixSum = 0;
    let ans = -Infinity;

    for (let num of nums) {
        if (map.has(num - k)) {
            ans = Math.max(
                ans,
                prefixSum + num - map.get(num - k)
            );
        }
        if (map.has(num + k)) {
            ans = Math.max(
                ans,
                prefixSum + num - map.get(num + k)
            );
        }
        if (!map.has(num)) {
            map.set(num, prefixSum);
        } else {
            map.set(num, Math.min(map.get(num), prefixSum));
        }
        prefixSum += num;
    }
    return ans === -Infinity ? 0 : ans;
};

