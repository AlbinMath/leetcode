/**
 * @param {number[]} nums
 * @param {number} maxC
 * @return {number}
 */
var minStable = function(nums, maxC) {
    const n = nums.length;

    // Edge case: can we eliminate ALL elements >= 2 (stability factor = 0)?
    let countGe2 = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] >= 2) countGe2++;
    }
    if (countGe2 <= maxC) return 0;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Build Sparse Table for O(1) range GCD queries
    const LOG = 32 - Math.clz32(n);
    const st = Array.from({ length: LOG }, () => new Int32Array(n));
    st[0].set(nums);

    for (let k = 1; k < LOG; k++) {
        const half = 1 << (k - 1);
        const limit = n - (1 << k);
        for (let i = 0; i <= limit; i++) {
            st[k][i] = gcd(st[k - 1][i], st[k - 1][i + half]);
        }
    }

    const lg = new Int32Array(n + 1);
    for (let i = 2; i <= n; i++) {
        lg[i] = lg[i >> 1] + 1;
    }

    const queryGcd = (l, r) => {
        const k = lg[r - l + 1];
        return gcd(st[k][l], st[k][r - (1 << k) + 1]);
    };

    // Check if we can break all stable subarrays of length L + 1 using <= maxC changes
    const canAchieve = (L) => {
        const windowLen = L + 1;
        let ops = 0;
        let lastModified = -1;

        for (let i = windowLen - 1; i < n; i++) {
            // Skip if this window already includes a modified element (set to 1)
            if (lastModified >= i - windowLen + 1) continue;

            if (queryGcd(i - windowLen + 1, i) >= 2) {
                ops++;
                if (ops > maxC) return false;
                lastModified = i;
            }
        }
        return true;
    };

    // Binary search for the minimum achievable stability factor L in [1, n]
    let low = 1;
    let high = n;
    let ans = n;

    while (low <= high) {
        const mid = (low + high) >> 1;
        if (canAchieve(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return ans;
};
