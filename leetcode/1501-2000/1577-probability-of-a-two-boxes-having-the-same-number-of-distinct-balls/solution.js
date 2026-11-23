var getProbability = function(balls) {
    const n = balls.reduce((sum, x) => sum + x, 0) / 2;
    const k = balls.length;

    const fact = new Array(49).fill(1);
    for (let i = 1; i < fact.length; i++) {
        fact[i] = fact[i - 1] * i;
    }

    let totalWays = 0;
    let validWays = 0;

    const dfs = (idx, box1Count, box2Count, distinct1, distinct2, ways) => {
        if (box1Count > n || box2Count > n) return;

        if (idx === k) {
            if (box1Count === n && box2Count === n) {
                totalWays += ways;
                if (distinct1 === distinct2) {
                    validWays += ways;
                }
            }
            return;
        }

        const ballsOfColor = balls[idx];

        for (let take = 0; take <= ballsOfColor; take++) {
            const remaining = ballsOfColor - take;

            dfs(
                idx + 1,
                box1Count + take,
                box2Count + remaining,
                distinct1 + (take > 0 ? 1 : 0),
                distinct2 + (remaining > 0 ? 1 : 0),
                ways / (fact[take] * fact[remaining])
            );
        }
    };

    dfs(0, 0, 0, 0, 0, fact[n] * fact[n]);

    return validWays / totalWays;
};
