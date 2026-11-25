
var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    const MAX = 50001;

    const graph = Array.from({ length: n }, () => []);

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }

    function add(bit, pos, delta) {
        for (let i = pos + 1; i <= n; i += i & -i) {
            bit[i] += delta;
        }
    }

    function query(bit, pos) {
        let result = 0;

        for (let i = pos; i > 0; i -= i & -i) {
            result += bit[i];
        }

        return result;
    }

    function kth(bit, k) {
        let index = 0;
        let step = 1;

        while (step * 2 <= n) step *= 2;

        for (; step > 0; step >>= 1) {
            const next = index + step;

            if (next <= n && bit[next] < k) {
                index = next;
                k -= bit[next];
            }
        }

        return index;
    }

    const duplicateBIT = new Array(n + 1).fill(0);
    const tripleBIT = new Array(n + 1).fill(0);

    const occurrences = Array.from(
        { length: MAX },
        () => []
    );

    const dist = new Array(n).fill(0);

    let bestLength = 0;
    let minNodes = 1;

    function update(value, depth, entering) {
        const arr = occurrences[value];
        const len = arr.length;

        if (entering) {
            if (len >= 2) {
                add(duplicateBIT, arr[len - 2], -1);
            }

            if (len >= 3) {
                add(tripleBIT, arr[len - 3], -1);
            }

            arr.push(depth);

            if (len >= 1) {
                add(duplicateBIT, arr[len - 1], 1);
            }

            if (len >= 2) {
                add(tripleBIT, arr[len - 2], 1);
            }
        } else {
            // Remove current markers
            if (len >= 2) {
                add(duplicateBIT, arr[len - 2], -1);
            }

            if (len >= 3) {
                add(tripleBIT, arr[len - 3], -1);
            }

            arr.pop();

            // Restore previous markers using corrected indices
            if (len - 1 >= 2) {
                add(duplicateBIT, arr[len - 3], 1);
            }

            if (len - 1 >= 3) {
                add(tripleBIT, arr[len - 4], 1);
            }
        }
    }

    const stack = [{
        node: 0,
        parent: -1,
        depth: 0,
        distance: 0,
        exit: false
    }];

    while (stack.length > 0) {
        const cur = stack.pop();

        const {
            node,
            parent,
            depth,
            distance
        } = cur;

        const value = nums[node];

        if (cur.exit) {
            update(value, depth, false);
            continue;
        }

        update(value, depth, true);

        dist[depth] = distance;

        let left = 0;

        // No value may occur three or more times.
        const tripleCount = query(tripleBIT, n);

        if (tripleCount > 0) {
            left = kth(tripleBIT, tripleCount) + 1;
        }

        // At most one value may occur twice.
        const duplicateCount = query(duplicateBIT, n);

        if (duplicateCount >= 2) {
            const position = kth(
                duplicateBIT,
                duplicateCount - 1
            );

            left = Math.max(left, position + 1);
        }

        const pathLength = distance - dist[left];
        const nodeCount = depth - left + 1;

        if (pathLength > bestLength) {
            bestLength = pathLength;
            minNodes = nodeCount;
        } else if (pathLength === bestLength) {
            minNodes = Math.min(minNodes, nodeCount);
        }

        // Backtracking event
        stack.push({
            node,
            depth,
            exit: true
        });

        for (const [v, w] of graph[node]) {
            if (v !== parent) {
                stack.push({
                    node: v,
                    parent: node,
                    depth: depth + 1,
                    distance: distance + w,
                    exit: false
                });
            }
        }
    }

    return [bestLength, minNodes];
};

