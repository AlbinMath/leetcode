
var maxValidSplits = function(nums) {
    const n = nums.length;
    if (n < 2) return 0;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // 1. Precompute prefix and suffix GCDs
    const pref = new Int32Array(n);
    const suff = new Int32Array(n);

    pref[0] = nums[0];
    for (let i = 1; i < n; i++) {
        pref[i] = gcd(pref[i - 1], nums[i]);
    }

    suff[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suff[i] = gcd(suff[i + 1], nums[i]);
    }

    const gAll = pref[n - 1];

    // Case 1: 0 removals (every valid split must have both sides equal to gAll)
    let maxScore = 0;
    for (let i = 0; i < n - 1; i++) {
        if (pref[i] === gAll && suff[i + 1] === gAll) {
            maxScore++;
        }
    }

    if (n < 3) return maxScore;

    // Case 2: 1 removal (index k)
    // Any improvement over 0 removals requires G_k = gcd(nums without k) > gAll.
    // Because G_k > gAll = gcd(G_k, nums[k]), nums[k] is the UNIQUE element in nums
    // not divisible by G_k. Thus each distinct G_k > gAll corresponds to a unique k,
    // and there are at most O(log(max(nums))) such indices k!
    const seenTargets = new Set();

    const scoreWithout = (skip, targetG) => {
        // Compute suffix GCDs of the (n - 1)-length array without `skip`
        const m = n - 1;
        const suffArr = new Int32Array(m);
        let cur = 0;
        let idx = m - 1;
        for (let j = n - 1; j >= 0; j--) {
            if (j === skip) continue;
            cur = gcd(cur, nums[j]);
            suffArr[idx--] = cur;
        }

        // Sweep prefix GCDs and count valid splits where pref == suff == targetG
        let valid = 0;
        cur = 0;
        idx = 0;
        for (let j = 0; j < n; j++) {
            if (j === skip) continue;
            cur = gcd(cur, nums[j]);
            if (idx < m - 1 && cur === targetG && suffArr[idx + 1] === targetG) {
                valid++;
            }
            idx++;
        }
        return valid;
    };

    for (let k = 0; k < n; k++) {
        const leftG = k > 0 ? pref[k - 1] : 0;
        const rightG = k < n - 1 ? suff[k + 1] : 0;
        const gWithoutK = gcd(leftG, rightG);

        if (gWithoutK > gAll && !seenTargets.has(gWithoutK)) {
            seenTargets.add(gWithoutK);
            const score = scoreWithout(k, gWithoutK);
            if (score > maxScore) {
                maxScore = score;
            }
        }
    }

    return maxScore;
};
