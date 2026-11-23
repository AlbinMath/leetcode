/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var popcountDepth = function (n, k) {
    if (k === 0) return 1; // only x = 1 has depth 0, and n >= 1

    const s = n.toString(2);
    const len = s.length;

    const pc = (x) => x.toString(2).replace(/0/g, "").length;

    const depth = new Array(len + 1).fill(0);
    for (let i = 2; i <= len; i++) depth[i] = depth[pc(i)] + 1;

    const C = Array.from({ length: len + 1 }, () => new Array(len + 1).fill(0));
    for (let i = 0; i <= len; i++) {
        C[i][0] = 1;
        for (let j = 1; j <= i; j++) C[i][j] = C[i - 1][j - 1] + (C[i - 1][j] || 0);
    }

    let ans = 0;
    for (let ones = 1; ones <= len; ones++) {
        if (depth[ones] !== k - 1) continue;

        let remaining = ones;
        for (let i = 0; i < len; i++) {
            if (s[i] === "1") {
                const left = len - i - 1;
                if (remaining <= left) ans += C[left][remaining];
                remaining--;
                if (remaining < 0) break;
            }
        }
        if (remaining === 0) ans++;
    }

    if (k === 1) ans--; // remove x = 1 (popcount 1 but depth 0)
    return ans;
};
