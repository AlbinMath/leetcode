
var TreeAncestor = function(n, parent) {
    this.LOG = 16;
    this.up = Array.from(
        { length: n },
        () => Array(this.LOG).fill(-1)
    );

    for (let i = 0; i < n; i++) {
        this.up[i][0] = parent[i];
    }

    for (let j = 1; j < this.LOG; j++) {
        for (let i = 0; i < n; i++) {
            const prev = this.up[i][j - 1];

            if (prev !== -1) {
                this.up[i][j] = this.up[prev][j - 1];
            }
        }
    }
};

TreeAncestor.prototype.getKthAncestor = function(node, k) {
    let bit = 0;

    while (k > 0 && node !== -1) {
        if (k & 1) {
            node = this.up[node][bit];
        }

        k >>= 1;
        bit++;
    }

    return node;
};

