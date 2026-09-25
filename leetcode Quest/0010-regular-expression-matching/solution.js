/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const memo = new Map();

    function dp(i, j) {
        // Pattern completely processed
        if (j === p.length) {
            return i === s.length;
        }

        const key = i + "," + j;
        if (memo.has(key)) {
            return memo.get(key);
        }

        // Check if current characters match
        const firstMatch =
            i < s.length &&
            (s[i] === p[j] || p[j] === ".");

        let result;

        // If next character is '*'
        if (j + 1 < p.length && p[j + 1] === "*") {
            // Option 1: use '*' as zero occurrences
            // Option 2: consume one matching character
            result =
                dp(i, j + 2) ||
                (firstMatch && dp(i + 1, j));
        } else {
            // Normal character or '.'
            result = firstMatch && dp(i + 1, j + 1);
        }

        memo.set(key, result);
        return result;
    }

    return dp(0, 0);
};
