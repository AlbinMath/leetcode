
var minimumFuelCost = function(roads, seats) {
    const n = roads.length + 1;

    if (n === 1) return 0;

    // Build adjacency list.
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of roads) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 1: Build parent relationships and DFS order.
    const parent = new Array(n).fill(-1);
    const order = [0];

    parent[0] = -2;

    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const v of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            order.push(v);
        }
    }

    // Each city initially has one representative.
    const people = new Array(n).fill(1);

    let fuel = 0;

    // Step 2: Process nodes from leaves to root.
    for (let i = order.length - 1; i > 0; i--) {
        const u = order[i];
        const p = parent[u];

        // Cars needed to move people from u to its parent.
        fuel += Math.ceil(people[u] / seats);

        // Add subtree representatives to the parent.
        people[p] += people[u];
    }

    return fuel;
};

