/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var maxStability = function(n, edges, k) {
    class DSU {
        constructor(n) {
            this.parent = Array.from({ length: n }, (_, i) => i);
            this.rank = new Array(n).fill(0);
            this.components = n;
        }

        find(x) {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }

        union(a, b) {
            a = this.find(a);
            b = this.find(b);

            if (a === b) return false;

            if (this.rank[a] < this.rank[b]) {
                [a, b] = [b, a];
            }

            this.parent[b] = a;

            if (this.rank[a] === this.rank[b]) {
                this.rank[a]++;
            }

            this.components--;
            return true;
        }
    }

    const mandatoryDSU = new DSU(n);
    let mandatoryMin = Infinity;

    for (const [u, v, s, must] of edges) {
        if (must === 1) {
            if (!mandatoryDSU.union(u, v)) return -1;
            mandatoryMin = Math.min(mandatoryMin, s);
        }
    }

    function canAchieve(target) {
        if (mandatoryMin < target) return false;

        const dsu = new DSU(n);

        for (const [u, v, s, must] of edges) {
            if (must === 1) {
                dsu.union(u, v);
            }
        }

        for (const [u, v, s, must] of edges) {
            if (must === 0 && s >= target) {
                dsu.union(u, v);
            }
        }

        let upgrades = 0;

        for (const [u, v, s, must] of edges) {
            if (must === 0 && s < target && 2 * s >= target) {
                if (dsu.union(u, v)) {
                    upgrades++;
                }
            }
        }

        return dsu.components === 1 && upgrades <= k;
    }

    let left = 1;
    let right = 200000;
    let answer = -1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (canAchieve(mid)) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return answer;
};
