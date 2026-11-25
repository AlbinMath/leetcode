
var minimumWhiteTiles = function(floor, numCarpets, carpetLen) {
    const n = floor.length;
    const dp = Array.from(
        { length: n + 1 },
        () => Array(numCarpets + 1).fill(0)
    );
    for (let i = 1; i <= n; i++) {
        dp[i][0] = dp[i - 1][0] + (floor[i - 1] === '1' ? 1 : 0);
    }
    for (let i = 1; i <= n; i++) {
        for (let k = 1; k <= numCarpets; k++) {
            let noCarpet = dp[i - 1][k];

            if (floor[i - 1] === '1') {
                noCarpet++;
            }
            let useCarpet = dp[Math.max(0, i - carpetLen)][k - 1];
            dp[i][k] = Math.min(noCarpet, useCarpet);
        }
    }

    return dp[n][numCarpets];
};
