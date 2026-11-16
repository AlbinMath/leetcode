
var maxValidSplits = function(nums) {
    const n = nums.length;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    const countSplits = (arr) => {
        const m = arr.length;
        if (m < 2) return 0;

        const pref = new Int32Array(m);
        const suff = new Int32Array(m);

        pref[0] = arr[0];
        for (let i = 1; i < m; i++) {
            pref[i] = gcd(pref[i - 1], arr[i]);
        }

        suff[m - 1] = arr[m - 1];
        for (let i = m - 2; i >= 0; i--) {
            suff[i] = gcd(suff[i + 1], arr[i]);
        }

        let valid = 0;
        for (let i = 0; i < m - 1; i++) {
            if (pref[i] === suff[i + 1]) {
                valid++;
            }
        }
        return valid;
    };

    // Case 1: Remove 0 elements
    let maxScore = countSplits(nums);

    // Case 2: Remove 1 element (only yields m >= 2 when n >= 3)
    if (n >= 3) {
        const arr = new Int32Array(n - 1);
        for (let skip = 0; skip < n; skip++) {
            let idx = 0;
            for (let j = 0; j < n; j++) {
                if (j !== skip) {
                    arr[idx++] = nums[j];
                }
            }
            const score = countSplits(arr);
            if (score > maxScore) {
                maxScore = score;
            }
        }
    }

    return maxScore;
};
