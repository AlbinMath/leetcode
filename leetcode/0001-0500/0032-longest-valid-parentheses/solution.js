
var longestValidParentheses = function(s) {
    const n = s.length;
    const dp = Array(n).fill(0);
    let maxLength = 0;

    for (let i = 1; i < n; i++) {
        if (s[i] === ')') {
            if (s[i - 1] === '(') {
                // Pattern: ...()
                dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
            } else if (i - dp[i - 1] - 1 >= 0 &&
                       s[i - dp[i - 1] - 1] === '(') {
                // Pattern: ...))
                const previousLength = dp[i - 1];
                const matchingOpen = i - previousLength - 1;

                dp[i] = previousLength + 2 +
                    (matchingOpen > 0 ? dp[matchingOpen - 1] : 0);
            }

            maxLength = Math.max(maxLength, dp[i]);
        }
    }

    return maxLength;
};

