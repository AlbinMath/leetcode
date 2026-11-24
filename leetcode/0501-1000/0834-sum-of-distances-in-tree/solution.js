
var sumOfDistancesInTree = function(n, edges) {
    // Step 1: Build adjacency list
    let graph = Array.from({ length: n }, () => []);

    for (let [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    let parent = new Array(n).fill(-1);
    let size = new Array(n).fill(1);
    let answer = new Array(n).fill(0);
    let order = [0];

    parent[0] = -2;

    // Step 2: Build traversal order and calculate depths
    for (let i = 0; i < order.length; i++) {
        let node = order[i];

        for (let child of graph[node]) {
            if (child === parent[node]) continue;

            parent[child] = node;
            order.push(child);

            answer[0] += 1;
        }
    }

    // Calculate total distance from root
    // using each node's depth
    let depth = new Array(n).fill(0);

    for (let node of order) {
        if (parent[node] >= 0) {
            depth[node] = depth[parent[node]] + 1;
        }
    }

    answer[0] = depth.reduce((sum, d) => sum + d, 0);

    // Step 3: Calculate subtree sizes (bottom-up)
    for (let i = n - 1; i > 0; i--) {
        let node = order[i];
        size[parent[node]] += size[node];
    }

    // Step 4: Reroot DP (top-down)
    for (let i = 1; i < n; i++) {
        let node = order[i];
        let p = parent[node];

        answer[node] = answer[p] - size[node] + (n - size[node]);
    }

    return answer;
};

