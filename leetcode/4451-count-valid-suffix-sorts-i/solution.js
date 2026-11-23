
var countSuffix = function(nums, target) {
    let n = nums.length;

    let freq = new Int32Array(100001);
    let nonZero = 0;

    // Calculate frequency differences
    for (let i = 0; i < n; i++) {
        freq[nums[i]]++;
        freq[target[i]]--;
    }

    for (let i = 1; i <= 100000; i++) {
        if (freq[i] !== 0) {
            nonZero++;
        }
    }

    // Check non-increasing target suffixes
    let sorted = new Array(n).fill(true);

    for (let i = n - 2; i >= 0; i--) {
        sorted[i] = sorted[i + 1] &&
                    target[i] >= target[i + 1];
    }

    let ans = 0;
    let prefixMatch = true;

    for (let i = 0; i < n; i++) {

        if (prefixMatch && nonZero === 0 && sorted[i]) {
            ans++;
        }

        let a = nums[i];
        let b = target[i];

        if (freq[a] !== 0) nonZero--;
        freq[a]--;
        if (freq[a] !== 0) nonZero++;

        if (freq[b] !== 0) nonZero--;
        freq[b]++;
        if (freq[b] !== 0) nonZero++;

        if (nums[i] !== target[i]) {
            prefixMatch = false;
        }
    }

    return ans;
};

