
var palindromePath = function (n, edges, s, queries) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const LOG = Math.max(1, 32 - Math.clz32(n - 1));
    const up = Array.from({ length: LOG }, () => new Int32Array(n));
    const depth = new Int32Array(n);
    const tin = new Int32Array(n);
    const tout = new Int32Array(n);
    const mask = new Int32Array(n);
    for (let i = 0; i < n; i++) mask[i] = 1 << (s.charCodeAt(i) - 97);

    // Iterative DFS: push node for "enter", ~node for "exit"
    let timer = 0;
    const stack = [0];
    up[0][0] = 0;
    while (stack.length) {
        const top = stack.pop();
        if (top < 0) {
            tout[~top] = timer - 1;
            continue;
        }
        const node = top;
        tin[node] = timer++;
        stack.push(~node);
        const par = up[0][node];
        for (const nb of adj[node]) {
            if (nb !== par || (node === 0 && nb !== 0 && false)) {
                if (nb === par && node !== 0) continue;
            }
            if (nb === par && node !== 0) continue;
            if (node === 0 && nb === par) continue; // root's "parent" is itself; no self-loops in a tree
            up[0][nb] = node;
            depth[nb] = depth[node] + 1;
            stack.push(nb);
        }
    }

    for (let k = 1; k < LOG; k++) {
        const prev = up[k - 1], cur = up[k];
        for (let v = 0; v < n; v++) cur[v] = prev[prev[v]];
    }

    const lca = (a, b) => {
        if (depth[a] < depth[b]) { const t = a; a = b; b = t; }
        let diff = depth[a] - depth[b];
        for (let k = 0; diff > 0; k++, diff >>= 1) {
            if (diff & 1) a = up[k][a];
        }
        if (a === b) return a;
        for (let k = LOG - 1; k >= 0; k--) {
            if (up[k][a] !== up[k][b]) {
                a = up[k][a];
                b = up[k][b];
            }
        }
        return up[0][a];
    };

    // XOR Fenwick tree: range-xor update, point query
    const bit = new Int32Array(n + 2);
    const add = (i, val) => {
        for (i += 1; i <= n + 1; i += i & -i) bit[i] ^= val;
    };
    const prefix = (i) => {
        let res = 0;
        for (i += 1; i > 0; i -= i & -i) res ^= bit[i];
        return res;
    };
    const rangeXor = (l, r, val) => {
        add(l, val);
        add(r + 1, val);
    };

    for (let v = 0; v < n; v++) rangeXor(tin[v], tout[v], mask[v]);

    const ans = [];
    for (const q of queries) {
        const parts = q.split(" ");
        if (parts[0] === "update") {
            const x = parseInt(parts[1]);
            const nw = 1 << (parts[2].charCodeAt(0) - 97);
            const delta = mask[x] ^ nw;
            if (delta !== 0) {
                rangeXor(tin[x], tout[x], delta);
                mask[x] = nw;
            }
        } else {
            const u = parseInt(parts[1]);
            const v = parseInt(parts[2]);
            const l = lca(u, v);
            const m = prefix(tin[u]) ^ prefix(tin[v]) ^ mask[l];
            ans.push((m & (m - 1)) === 0);
        }
    }
    return ans;
};
