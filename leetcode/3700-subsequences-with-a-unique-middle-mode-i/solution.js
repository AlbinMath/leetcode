
var subsequencesWithMiddleMode = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;

    const C2 = a => a * (a - 1) / 2;
    const C = (a, b) => {
        if (b < 0 || b > a || a < 0) return 0;
        if (b === 0) return 1;
        if (b === 1) return a;
        if (b === 2) return C2(a);
        return a * (a - 1) * (a - 2) / 6;
    };

    const left = new Map();
    const right = new Map();

    for (const v of nums) {
        right.set(v, (right.get(v) || 0) + 1);
    }

    let ans = 0;

    for (let mid = 0; mid < n; mid++) {
        const x = nums[mid];

        right.set(x, right.get(x) - 1);
        if (right.get(x) === 0) right.delete(x);

        const L = mid;
        const R = n - mid - 1;
        const lx = left.get(x) || 0;
        const rx = right.get(x) || 0;

        if (L >= 2 && R >= 2) {
            const ol = L - lx;
            const or = R - rx;

            // Case 1: x appears at least 3 times.
            let ways = 0;

            for (let i = 0; i <= 2; i++) {
                for (let j = 0; j <= 2; j++) {
                    if (i + j < 2) continue;

                    ways += C(lx, i) * C(ol, 2 - i)
                          * C(rx, j) * C(or, 2 - j);
                }
            }

            // Case 2: x appears exactly twice.
            // x is selected once from the left, or once from the right.
            let dupL = 0;
            let dupR = 0;

            for (const [v, count] of left) {
                if (v !== x) dupL += C2(count);
            }
            for (const [v, count] of right) {
                if (v !== x) dupR += C2(count);
            }

            // One x from the left, then one distinct left value
            // and two distinct right values, all mutually distinct.
            for (const [v, lv] of left) {
                if (v === x) continue;
                const rv = right.get(v) || 0;
                const validRightPairs =
                    C2(or) - dupR - rv * (or - rv);

                ways += lx * lv * validRightPairs;
            }

            // One x from the right, then two distinct left values
            // and one distinct right value, all mutually distinct.
            for (const [v, rv] of right) {
                if (v === x) continue;
                const lv = left.get(v) || 0;
                const validLeftPairs =
                    C2(ol) - dupL - lv * (ol - lv);

                ways += rx * rv * validLeftPairs;
            }

            ans = ((ans + ways) % MOD + MOD) % MOD;
        }

        left.set(x, (left.get(x) || 0) + 1);
    }

    return ans;
};

