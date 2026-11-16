
var countGoodSubseq = function(nums, p, queries) {
    const n = nums.length;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Normalized array: b[i] = nums[i] / p if divisible by p, else 0
    const b = new Int32Array(n);
    let divisibleCount = 0;

    for (let i = 0; i < n; i++) {
        if (nums[i] % p === 0) {
            b[i] = nums[i] / p;
            divisibleCount++;
        }
    }

    // Segment Tree storing GCD over b (identity element is 0)
    let size = 1;
    while (size < n) size <<= 1;
    const tree = new Int32Array(2 * size);

    for (let i = 0; i < n; i++) {
        tree[size + i] = b[i];
    }
    for (let i = size - 1; i >= 1; i--) {
        tree[i] = gcd(tree[i << 1], tree[(i << 1) | 1]);
    }

    const update = (idx, val) => {
        let pos = size + idx;
        tree[pos] = val;
        for (pos >>= 1; pos >= 1; pos >>= 1) {
            tree[pos] = gcd(tree[pos << 1], tree[(pos << 1) | 1]);
        }
    };

    const hasGoodSubsequence = () => {
        // Must have at least one multiple of p, and total GCD of multiples must be 1
        if (divisibleCount === 0 || tree[1] !== 1) return false;

        // If at least one element is not divisible by p, taking all divisible elements has length < n
        if (divisibleCount < n) return true;

        // All n elements are divisible by p (divisibleCount === n):
        // Since b[i] <= 50000 has at most 6 prime factors, for n >= 8 there is always
        // an index i whose removal leaves GCD == 1 whenever total GCD == 1.
        if (n >= 8) return true;

        // For 2 <= n <= 7, explicitly check removing each index i
        for (let skip = 0; skip < n; skip++) {
            let g = 0;
            for (let j = 0; j < n; j++) {
                if (j !== skip) g = gcd(g, b[j]);
            }
            if (g === 1) return true;
        }
        return false;
    };

    let goodQueries = 0;

    for (let q = 0; q < queries.length; q++) {
        const [idx, val] = queries[q];

        if (b[idx] > 0) divisibleCount--;
        const nextB = (val % p === 0) ? (val / p) : 0;
        b[idx] = nextB;
        if (nextB > 0) divisibleCount++;

        update(idx, nextB);

        if (hasGoodSubsequence()) {
            goodQueries++;
        }
    }

    return goodQueries;
};
