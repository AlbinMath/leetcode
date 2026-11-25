var maxValueOfCoins = function(piles, k) {
    let dp = Array(k + 1).fill(-Infinity);
    dp[0] = 0;
    for (let pile of piles) {
        let prefix = [0];
        for (let coin of pile) {
            prefix.push(prefix[prefix.length - 1] + coin);
        }
        let newDp = Array(k + 1).fill(-Infinity);
        for (let j = 0; j <= k; j++) {
            for (let x = 0; x <= Math.min(j, pile.length); x++) {
                if (dp[j - x] !== -Infinity) {
                    newDp[j] = Math.max(
                        newDp[j],
                        dp[j - x] + prefix[x]
                    );
                }
            }
        }
        dp = newDp;
    }
    return dp[k];
};
