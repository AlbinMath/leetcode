/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var matrixRankTransform = function (matrix) {
    const m = matrix.length, n = matrix[0].length;
    const parent = new Int32Array(m + n);
    for (let i = 0; i < m + n; i++) parent[i] = i;
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };

    const cells = [];
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) cells.push(i * n + j);
    cells.sort((a, b) => matrix[(a / n) | 0][a % n] - matrix[(b / n) | 0][b % n]);

    const rowRank = new Int32Array(m);
    const colRank = new Int32Array(n);
    const ans = Array.from({ length: m }, () => new Array(n).fill(0));
    const compMax = new Int32Array(m + n);

    let p = 0;
    const total = cells.length;
    while (p < total) {
        let q = p;
        const val = matrix[(cells[p] / n) | 0][cells[p] % n];
        while (q < total && matrix[(cells[q] / n) | 0][cells[q] % n] === val) q++;

        // union rows and columns of equal-valued cells
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            const a = find(i), b = find(m + j);
            if (a !== b) parent[a] = b;
        }

        // component max of existing ranks
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            const root = find(i);
            compMax[root] = 0;
        }
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            const root = find(i);
            const cur = Math.max(rowRank[i], colRank[j]);
            if (cur > compMax[root]) compMax[root] = cur;
        }

        // assign ranks
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            ans[i][j] = compMax[find(i)] + 1;
        }
        // update row and column ranks after all assignments
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            rowRank[i] = ans[i][j];
            colRank[j] = ans[i][j];
        }

        // reset union-find for touched nodes
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            parent[i] = i;
            parent[m + j] = m + j;
        }
        p = q;
    }
    return ans;
};
