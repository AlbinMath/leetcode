
var shortestDistanceAfterQueries = function(n, queries) {
    const next = new Array(n);

    for (let i = 0; i < n; i++) {
        next[i] = i + 1;
    }

    let distance = n - 1;
    const answer = [];

    for (const [u, v] of queries) {

        // Ignore the query if either endpoint was removed.
        if (next[u] === -1 || next[v] === -1) {
            answer.push(distance);
            continue;
        }

        // Remove all active cities between u and v.
        let city = next[u];

        while (city !== v) {
            const following = next[city];

            next[city] = -1;
            distance--;

            city = following;
        }

        // Connect u directly to v.
        next[u] = v;

        answer.push(distance);
    }

    return answer;
};

