
/**
 * @param {number[]} tasks
 * @param {number} sessionTime
 * @return {number}
 */
var minSessions = function(tasks, sessionTime) {
    const n = tasks.length;
    const totalMasks = 1 << n;

    // dp[mask] = [number of sessions, time used in last session]
    const dp = Array.from(
        { length: totalMasks },
        () => [Infinity, Infinity]
    );

    dp[0] = [0, 0];

    for (let mask = 0; mask < totalMasks; mask++) {
        const [sessions, used] = dp[mask];

        if (sessions === Infinity) continue;

        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;

            const nextMask = mask | (1 << i);
            let nextSessions;
            let nextUsed;

            if (sessions === 0) {
                nextSessions = 1;
                nextUsed = tasks[i];
            } else if (used + tasks[i] <= sessionTime) {
                nextSessions = sessions;
                nextUsed = used + tasks[i];
            } else {
                nextSessions = sessions + 1;
                nextUsed = tasks[i];
            }

            const [oldSessions, oldUsed] = dp[nextMask];

            if (
                nextSessions < oldSessions ||
                (nextSessions === oldSessions && nextUsed < oldUsed)
            ) {
                dp[nextMask] = [nextSessions, nextUsed];
            }
        }
    }

    return dp[totalMasks - 1][0];
};

