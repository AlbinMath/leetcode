var possibleStringCount = function(word, k) {
    const MOD = 1000000007;
    const n = word.length;
    const groups = [];
    let total = 1;
    let count = 1;
    for (let i = 1; i < n; i++) {
        if (word[i] === word[i - 1]) {
            count++;
        } else {
            groups.push(count);
            total = (total * count) % MOD;
            count = 1;
        }
    }
    groups.push(count);
    total = (total * count) % MOD;
    const m = groups.length;
    if (m >= k) {
        return total;
    }
    let dp = new Array(k).fill(0);
    dp[0] = 1;
    for (const len of groups) {
        const ndp = new Array(k).fill(0);
        let window = 0;
        for (let s = 0; s < k; s++) {
            if (s >= 1) {
                window = (window + dp[s - 1]) % MOD;
            }
            if (s - len - 1 >= 0) {
                window = (
                    window - dp[s - len - 1] + MOD
                ) % MOD;
            }
            ndp[s] = window;
        }
        dp = ndp;
    }
    let invalid = 0;

    for (let s = 0; s < k; s++) {
        invalid = (invalid + dp[s]) % MOD;
    }
    return (total - invalid + MOD) % MOD;
};

