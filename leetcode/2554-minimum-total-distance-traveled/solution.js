
var minimumTotalDistance = function(robot, factory) {
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);

    const n = robot.length;

    let dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    for (const [position, limit] of factory) {
        const newDp = new Array(n + 1).fill(Infinity);

        for (let i = 0; i <= n; i++) {
            let distance = 0;

            for (let count = 0; count <= Math.min(i, limit); count++) {
                if (count > 0) {
                    distance += Math.abs(
                        robot[i - count] - position
                    );
                }

                newDp[i] = Math.min(
                    newDp[i],
                    dp[i - count] + distance
                );
            }
        }

        dp = newDp;
    }

    return dp[n];
};

