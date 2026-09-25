/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxPalindromes = function(s, k) {
    const n = s.length;

    // dp[i] = maximum number of valid palindromes
    // using the first i characters.
    const dp = new Array(n + 1).fill(0);

    // palindrome[l][r] = true if s[l...r] is a palindrome
    const palindrome = Array.from(
        { length: n },
        () => new Array(n).fill(false)
    );

    // Build palindrome table
    for (let len = 1; len <= n; len++) {
        for (let l = 0; l + len <= n; l++) {
            const r = l + len - 1;

            if (
                s[l] === s[r] &&
                (len <= 2 || palindrome[l + 1][r - 1])
            ) {
                palindrome[l][r] = true;
            }
        }
    }

    // Find the maximum number of non-overlapping palindromes
    for (let i = 1; i <= n; i++) {
        // Don't take a palindrome ending at i
        dp[i] = dp[i - 1];

        for (let len = k; len <= i; len++) {
            const l = i - len;
            const r = i - 1;

            if (palindrome[l][r]) {
                dp[i] = Math.max(dp[i], dp[l] + 1);
            }
        }
    }

    return dp[n];
};
