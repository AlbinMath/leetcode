
var maxLen = function(n, edges, label) {
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const totalStates = (1 << n) * n * n;
    const visited = new Uint8Array(totalStates);

    let answer = 1;

    function dfs(mask, u, v, len) {
        const key = (mask * n + u) * n + v;

        if (visited[key]) return;
        visited[key] = 1;

        answer = Math.max(answer, len);

        // Expand both endpoints.
        for (const x of graph[u]) {
            if (mask & (1 << x)) continue;

            for (const y of graph[v]) {
                if (mask & (1 << y)) continue;
                if (x === y) continue;

                // Both new endpoints must have matching labels.
                if (label[x] !== label[y]) continue;

                const newMask = mask | (1 << x) | (1 << y);

                // Store endpoints in a canonical order.
                const a = Math.min(x, y);
                const b = Math.max(x, y);

                dfs(newMask, a, b, len + 2);
            }
        }
    }

    // Odd-length palindromes: start from one vertex.
    for (let i = 0; i < n; i++) {
        dfs(1 << i, i, i, 1);
    }

    // Even-length palindromes: start from an edge
    // whose endpoint labels are equal.
    for (const [u, v] of edges) {
        if (label[u] === label[v]) {
            const mask = (1 << u) | (1 << v);

            const a = Math.min(u, v);
            const b = Math.max(u, v);

            dfs(mask, a, b, 2);
        }
    }

    return answer;
};

