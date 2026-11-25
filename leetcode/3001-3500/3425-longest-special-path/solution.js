
var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }
    const lastSeen = new Array(50001).fill(-1);
    const distAtDepth = new Array(n).fill(0);

    let bestLength = -1;
    let minNodes = Infinity;
    const stack = [{
        node: 0,
        parent: -1,
        depth: 0,
        dist: 0,
        left: 0,
        exit: false
    }];

    while (stack.length > 0) {
        const cur = stack.pop();

        const u = cur.node;
        const depth = cur.depth;

        if (cur.exit) {
            if (cur.previous === -1) {
                lastSeen[nums[u]] = -1;
            } else {
                lastSeen[nums[u]] = cur.previous;
            }
            continue;
        }

        const value = nums[u];
        const previous = lastSeen[value];
        let left = cur.left;

        if (previous !== -1) {
            left = Math.max(left, previous + 1);
        }
        lastSeen[value] = depth;
        distAtDepth[depth] = cur.dist;
        const length = cur.dist - distAtDepth[left];
        const nodes = depth - left + 1;

        if (length > bestLength) {
            bestLength = length;
            minNodes = nodes;
        } else if (length === bestLength) {
            minNodes = Math.min(minNodes, nodes);
        }
        stack.push({
            node: u,
            exit: true,
            previous: previous
        });
        for (const [v, w] of graph[u]) {
            if (v === cur.parent) continue;

            stack.push({
                node: v,
                parent: u,
                depth: depth + 1,
                dist: cur.dist + w,
                left: left,
                exit: false
            });
        }
    }

    return [bestLength, minNodes];
};

