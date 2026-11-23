/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} nums
 * @return {number}
 */
var sumOfAncestors = function(n, edges, nums) {
    const MAX_VAL = 100000;

    // 1. Build Smallest Prime Factor (SPF) sieve up to 100,000
    const spf = new Int32Array(MAX_VAL + 1);
    for (let i = 2; i <= MAX_VAL; i++) {
        if (spf[i] === 0) {
            for (let j = i; j <= MAX_VAL; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    // Helper to compute the square-free kernel of x
    const getKernel = (x) => {
        let kernel = 1;
        while (x > 1) {
            const p = spf[x];
            let odd = false;
            while (x % p === 0) {
                x = Math.floor(x / p);
                odd = !odd;
            }
            if (odd) kernel *= p;
        }
        return kernel;
    };

    // 2. Transform nums[i] into its square-free kernel
    const kernels = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        kernels[i] = getKernel(nums[i]);
    }

    // 3. Build adjacency list for the tree
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
        const [u, v] = edges[i];
        adj[u].push(v);
        adj[v].push(u);
    }

    // 4. Iterative DFS with backtracking to avoid call stack limits on deep trees
    const freq = new Int32Array(MAX_VAL + 1);
    const parent = new Int32Array(n).fill(-1);
    const edgeIdx = new Int32Array(n);
    const stack = [0];

    let total = 0;

    // Enter root 0 (root has no ancestors, so it adds 0 to total)
    freq[kernels[0]]++;

    while (stack.length > 0) {
        const u = stack[stack.length - 1];
        const neighbors = adj[u];

        if (edgeIdx[u] < neighbors.length) {
            const v = neighbors[edgeIdx[u]++];
            if (v === parent[u]) continue;

            parent[v] = u;
            const k = kernels[v];
            total += freq[k];
            freq[k]++;
            stack.push(v);
        } else {
            // Backtrack: remove u from the active ancestor path
            freq[kernels[u]]--;
            stack.pop();
        }
    }

    return total;
};
