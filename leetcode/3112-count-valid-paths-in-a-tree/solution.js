
var countPaths = function(n, edges) {
    // Step 1: Sieve of Eratosthenes
    const isPrime = new Uint8Array(n + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // Step 2: Build adjacency list
    const graph = Array.from({ length: n + 1 }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 3: Find sizes of non-prime components
    const componentSize = new Int32Array(n + 1);
    const visited = new Uint8Array(n + 1);

    for (let node = 1; node <= n; node++) {
        if (isPrime[node] || visited[node]) continue;

        let size = 0;
        const stack = [node];
        visited[node] = 1;

        while (stack.length > 0) {
            const curr = stack.pop();
            size++;

            for (const next of graph[curr]) {
                if (!isPrime[next] && !visited[next]) {
                    visited[next] = 1;
                    stack.push(next);
                }
            }
        }

        // Assign the component size to its nodes
        const nodes = [node];
        const seen = new Set(nodes);

        while (nodes.length > 0) {
            const curr = nodes.pop();
            componentSize[curr] = size;

            for (const next of graph[curr]) {
                if (!isPrime[next] && !seen.has(next)) {
                    seen.add(next);
                    nodes.push(next);
                }
            }
        }
    }

    // Step 4: Count paths containing exactly one prime
    let answer = 0;

    for (let prime = 2; prime <= n; prime++) {
        if (!isPrime[prime]) continue;

        let total = 0;

        for (const neighbor of graph[prime]) {
            if (isPrime[neighbor]) continue;

            const size = componentSize[neighbor];

            // Paths from this prime to this component
            answer += size;

            // Paths connecting two different components
            answer += total * size;

            total += size;
        }
    }

    return answer;
};

