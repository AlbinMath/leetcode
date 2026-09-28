function winnerSquareGame(n: number): boolean {
    const dp: boolean[] = new Array(n + 1).fill(false);

    // dp[i] = true means the current player can win with i stones

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j * j <= i; j++) {
            // If we can move to a losing state,
            // the current state is winning.
            if (!dp[i - j * j]) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
}
