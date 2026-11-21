
var findSubtreeSizes = function(parent, s) {
    const n = parent.length;
    const adj = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        adj[parent[i]].push(i);
    }

    const newParent = parent.slice();
    const lastSeen = new Int32Array(26).fill(-1);

    // Pass 1: Iterative pre-order DFS with explicit exit markers to avoid call-stack limits
    const stack = [[0, false]];
    while (stack.length > 0) {
        const frame = stack[stack.length - 1];
        const u = frame[0];
        const ch = s.charCodeAt(u) - 97;

        if (!frame[1]) {
            frame[1] = true;
            frame[2] = lastSeen[ch]; // Save previous ancestor on frame
            if (lastSeen[ch] !== -1) {
                newParent[u] = lastSeen[ch];
            }
            lastSeen[ch] = u;

            const children = adj[u];
            for (let i = children.length - 1; i >= 0; i--) {
                stack.push([children[i], false]);
            }
        } else {
            lastSeen[ch] = frame[2]; // Restore on exit
            stack.pop();
        }
    }

    // Build final tree adjacency list and compute subtree sizes bottom-up
    const finalAdj = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        finalAdj[newParent[i]].push(i);
    }

    const order = [];
    const dfsStack = [0];
    while (dfsStack.length > 0) {
        const u = dfsStack.pop();
        order.push(u);
        for (const v of finalAdj[u]) {
            dfsStack.push(v);
        }
    }

    const answer = new Array(n).fill(1);
    for (let i = order.length - 1; i >= 1; i--) {
        const u = order[i];
        answer[newParent[u]] += answer[u];
    }

    return answer;
};
