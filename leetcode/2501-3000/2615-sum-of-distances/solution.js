var distance = function(nums) {
    const n = nums.length;
    let map = new Map();
    for (let i = 0; i < n; i++) {
        if (!map.has(nums[i])) {
            map.set(nums[i], []);
        }
        map.get(nums[i]).push(i);
    }
    let result = new Array(n).fill(0);
    for (let indices of map.values()) {
        const m = indices.length;
        let prefix = new Array(m + 1).fill(0);

        for (let j = 0; j < m; j++) {
            prefix[j + 1] = prefix[j] + indices[j];
        }

        const totalSum = prefix[m];
        for (let j = 0; j < m; j++) {
            let pos = indices[j];
            let left = j * pos - prefix[j];
            let right =
                (totalSum - prefix[j + 1]) -
                (m - j - 1) * pos;

            result[pos] = left + right;
        }
    }
    return result;
};

