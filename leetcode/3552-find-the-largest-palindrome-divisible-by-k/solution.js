/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var largestPalindrome = function(n, k) {
    // Fast path for k = 1, 3, 9: all 9s is always divisible by 1, 3, and 9
    if (k === 1 || k === 3 || k === 9) {
        return '9'.repeat(n);
    }

    const half = Math.ceil(n / 2);

    // Precompute powers of 10 modulo k
    const pow10 = new Int32Array(n);
    pow10[0] = 1 % k;
    for (let i = 1; i < n; i++) {
        pow10[i] = (pow10[i - 1] * 10) % k;
    }

    // Precompute the modular weight of placing digit 1 at symmetric positions (i, n - 1 - i)
    const weight = new Int32Array(half);
    for (let i = 0; i < half; i++) {
        const j = n - 1 - i;
        weight[i] = (i === j) ? pow10[n - 1 - i] : (pow10[n - 1 - i] + pow10[i]) % k;
    }

    // visited[i * k + rem] = 1 if (i, rem) cannot form a valid palindrome
    const visited = new Uint8Array(half * k);
    const chosen = new Int32Array(half);

    const dfs = (i, rem) => {
        if (i === half) {
            return rem === 0;
        }

        const state = i * k + rem;
        if (visited[state]) {
            return false;
        }

        const minDigit = (i === 0) ? 1 : 0;
        const w = weight[i];

        // Try digits greedily from 9 down to minDigit
        for (let d = 9; d >= minDigit; d--) {
            const nextRem = (rem + d * w) % k;
            if (dfs(i + 1, nextRem)) {
                chosen[i] = d;
                return true;
            }
        }

        visited[state] = 1;
        return false;
    };

    dfs(0, 0);

    // Reconstruct the full n-digit palindrome string
    const res = new Array(n);
    for (let i = 0; i < half; i++) {
        const ch = String(chosen[i]);
        res[i] = ch;
        res[n - 1 - i] = ch;
    }

    return res.join('');
};
