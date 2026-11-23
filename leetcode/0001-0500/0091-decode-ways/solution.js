
var numDecodings = function(s) {
    const n = s.length;
    const dp = new Array(n + 1).fill(0);

    dp[0] = 1;

    for (let i = 1; i <= n; i++) {
        // Decode one digit
        if (s[i - 1] !== '0') {
            dp[i] += dp[i - 1];
        }

        // Decode two digits
        if (i >= 2) {
            const twoDigits = Number(s.substring(i - 2, i));

            if (twoDigits >= 10 && twoDigits <= 26) {
                dp[i] += dp[i - 2];
            }
        }
    }

    return dp[n];
};

