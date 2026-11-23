
var isScramble = function(s1, s2) {
    const memo = new Map();

    function dfs(a, b) {
        if (a === b) return true;

        if (a.length !== b.length) return false;

        const key = a + "|" + b;

        if (memo.has(key)) {
            return memo.get(key);
        }

        // Check whether both strings have the same characters
        const sortedA = a.split("").sort().join("");
        const sortedB = b.split("").sort().join("");

        if (sortedA !== sortedB) {
            memo.set(key, false);
            return false;
        }

        const n = a.length;

        for (let i = 1; i < n; i++) {
            // Case 1: No swap
            if (
                dfs(a.substring(0, i), b.substring(0, i)) &&
                dfs(a.substring(i), b.substring(i))
            ) {
                memo.set(key, true);
                return true;
            }

            // Case 2: Swap
            if (
                dfs(a.substring(0, i), b.substring(n - i)) &&
                dfs(a.substring(i), b.substring(0, n - i))
            ) {
                memo.set(key, true);
                return true;
            }
        }

        memo.set(key, false);
        return false;
    }

    return dfs(s1, s2);
};

