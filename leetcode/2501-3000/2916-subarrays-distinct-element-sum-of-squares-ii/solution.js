
var sumCounts = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;

    const sum = new Array(4 * n).fill(0);
    const sumSq = new Array(4 * n).fill(0);
    const lazy = new Array(4 * n).fill(0);

    function apply(node, left, right, delta) {
        const len = right - left + 1;

        sumSq[node] = (
            sumSq[node] +
            2 * delta * sum[node] +
            delta * delta * len
        ) % MOD;

        sum[node] = (sum[node] + delta * len) % MOD;
        lazy[node] += delta;
    }

    function push(node, left, right) {
        if (lazy[node] === 0 || left === right) return;

        const mid = Math.floor((left + right) / 2);
        const delta = lazy[node];

        apply(node * 2, left, mid, delta);
        apply(node * 2 + 1, mid + 1, right, delta);

        lazy[node] = 0;
    }

    function update(node, left, right, ql, qr) {
        if (ql > right || qr < left) return;

        if (ql <= left && right <= qr) {
            apply(node, left, right, 1);
            return;
        }

        push(node, left, right);

        const mid = Math.floor((left + right) / 2);

        update(node * 2, left, mid, ql, qr);
        update(node * 2 + 1, mid + 1, right, ql, qr);

        sum[node] = (
            sum[node * 2] + sum[node * 2 + 1]
        ) % MOD;

        sumSq[node] = (
            sumSq[node * 2] + sumSq[node * 2 + 1]
        ) % MOD;
    }

    const lastSeen = new Map();
    let answer = 0;

    for (let i = 0; i < n; i++) {
        const prev = lastSeen.has(nums[i])
            ? lastSeen.get(nums[i])
            : -1;

        update(1, 0, n - 1, prev + 1, i);

        lastSeen.set(nums[i], i);

        answer = (answer + sumSq[1]) % MOD;
    }

    return answer;
};

