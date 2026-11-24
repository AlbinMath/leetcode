
var maxWeight = function(n, edges, k, t) {
    if (k === 0) return 0;

    // dp[i]: bit s is 1 if a path ending at node i
    // can have total weight s using the current number of edges.
    let dp = new Array(n).fill(1n);

    // Keep only sums strictly less than t.
    const mask = (1n << BigInt(t)) - 1n;

    for (let step = 1; step <= k; step++) {
        const next = new Array(n).fill(0n);

        for (const [u, v, w] of edges) {
            // Shift all reachable sums by edge weight w.
            next[v] |= (dp[u] << BigInt(w)) & mask;
        }

        dp = next;
    }

    // Find the largest reachable sum.
    let answer = -1;

    for (let i = 0; i < n; i++) {
        if (dp[i] === 0n) continue;

        for (let sum = t - 1; sum >= 0; sum--) {
            if ((dp[i] & (1n << BigInt(sum))) !== 0n) {
                answer = Math.max(answer, sum);
                break;
            }
        }
    }

    return answer;
};

