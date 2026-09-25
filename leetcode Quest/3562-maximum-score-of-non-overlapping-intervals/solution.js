/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var maximumWeight = function(intervals) {
    const n = intervals.length;

    // [left, right, weight, originalIndex]
    const arr = intervals.map((x, i) => [x[0], x[1], x[2], i]);

    // Sort by right endpoint
    arr.sort((a, b) => {
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[0] - b[0];
    });

    // Find last interval with right < current left
    function findPrevious(pos) {
        let left = 0;
        let right = pos - 1;
        let ans = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (arr[mid][1] < arr[pos][0]) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return ans;
    }

    // Compare two sorted index arrays lexicographically
    function lexSmaller(a, b) {
        const len = Math.min(a.length, b.length);

        for (let i = 0; i < len; i++) {
            if (a[i] !== b[i]) {
                return a[i] < b[i];
            }
        }

        return a.length < b.length;
    }

    // Return better state
    function better(a, b) {
        if (a === null) return b;
        if (b === null) return a;

        if (a.score > b.score) return a;
        if (b.score > a.score) return b;

        return lexSmaller(a.indices, b.indices) ? a : b;
    }

    // dp[k][i]:
    // best result using exactly k intervals
    // from first i intervals
    const dp = Array.from(
        { length: 5 },
        () => Array(n + 1).fill(null)
    );

    // Choosing 0 intervals
    for (let i = 0; i <= n; i++) {
        dp[0][i] = {
            score: 0,
            indices: []
        };
    }

    for (let i = 1; i <= n; i++) {
        const cur = i - 1;
        const p = findPrevious(cur);

        for (let k = 1; k <= 4; k++) {

            // Don't choose current interval
            let best = dp[k][i - 1];

            // Choose current interval
            if (dp[k - 1][p + 1] !== null) {
                const prev = dp[k - 1][p + 1];

                // IMPORTANT:
                // Add original index and sort indices
                const newIndices = [
                    ...prev.indices,
                    arr[cur][3]
                ].sort((a, b) => a - b);

                const candidate = {
                    score: prev.score + arr[cur][2],
                    indices: newIndices
                };

                best = better(best, candidate);
            }

            dp[k][i] = best;
        }
    }

    // At most 4 intervals
    let answer = {
        score: 0,
        indices: []
    };

    for (let k = 1; k <= 4; k++) {
        answer = better(answer, dp[k][n]);
    }

    return answer.indices;
};
