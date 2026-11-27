
var minOperations = function(nums, locked, k) {
    const n = nums.length;

    let size = 1;
    while (size < n + 1) size *= 2;

    const INF = Infinity;
    const seg = new Array(2 * size).fill(INF);

    function update(value, index) {
        let p = value + size;
        seg[p] = index;

        while (p > 1) {
            p >>= 1;
            seg[p] = Math.min(seg[p * 2], seg[p * 2 + 1]);
        }
    }

    function query(left) {
        let l = left + size;
        let r = n + 1 + size;
        let result = INF;

        while (l < r) {
            if (l & 1) {
                result = Math.min(result, seg[l]);
                l++;
            }

            if (r & 1) {
                r--;
                result = Math.min(result, seg[r]);
            }

            l >>= 1;
            r >>= 1;
        }

        return result;
    }

    const diff = new Array(n + 1).fill(0);

    const bit = new Array(n + 1).fill(0);

    function bitQuery(index) {
        let sum = 0;

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    function bitUpdate(index) {
        while (index <= n) {
            bit[index]++;
            index += index & -index;
        }
    }

    let inversions = 0;

    for (let i = 0; i < n; i++) {
        const x = nums[i];

        const p = query(x + 1);

        if (p !== INF) {
            diff[p]++;
            diff[i + 1]--;
        }

        inversions += i - bitQuery(x);
        bitUpdate(x);

        update(x, i);
    }

    let active = 0;
    let unlocks = 0;

    for (let i = 0; i < n; i++) {
        active += diff[i];

        if (active > 0 && locked[i] === 1) {
            unlocks++;
        }
    }

    if (unlocks > k) {
        return -1;
    }

    return inversions + unlocks;
};

