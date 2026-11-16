/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var maximumCount = function(nums, queries) {
    const n = nums.length;
    const MAX_VAL = 100000;

    // 1. Sieve of Eratosthenes up to 100,000
    const isPrime = new Uint8Array(MAX_VAL + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;
    for (let i = 2; i * i <= MAX_VAL; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= MAX_VAL; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Lazy Segment Tree over split positions [1, n - 1]
    const tree = new Int32Array(4 * n);
    const lazy = new Int32Array(4 * n);

    const updateRange = (node, start, end, l, r, val) => {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }
        const mid = (start + end) >> 1;
        const leftChild = node << 1;
        const rightChild = leftChild | 1;

        if (lazy[node] !== 0) {
            tree[leftChild] += lazy[node];
            lazy[leftChild] += lazy[node];
            tree[rightChild] += lazy[node];
            lazy[rightChild] += lazy[node];
            lazy[node] = 0;
        }

        updateRange(leftChild, start, mid, l, r, val);
        updateRange(rightChild, mid + 1, end, l, r, val);
        tree[node] = Math.max(tree[leftChild], tree[rightChild]);
    };

    // 3. Lightweight Binary Heap for tracking min/max indices per prime
    class Heap {
        constructor(isMin) {
            this.data = [];
            this.isMin = isMin;
        }
        push(val) {
            const d = this.data;
            d.push(val);
            let i = d.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.isMin ? d[i] < d[p] : d[i] > d[p]) {
                    [d[i], d[p]] = [d[p], d[i]];
                    i = p;
                } else break;
            }
        }
        pop() {
            const d = this.data;
            const top = d[0];
            const last = d.pop();
            if (d.length > 0) {
                d[0] = last;
                let i = 0;
                const len = d.length;
                while (true) {
                    let best = i;
                    const l = (i << 1) + 1;
                    const r = l + 1;
                    if (l < len && (this.isMin ? d[l] < d[best] : d[l] > d[best])) best = l;
                    if (r < len && (this.isMin ? d[r] < d[best] : d[r] > d[best])) best = r;
                    if (best !== i) {
                        [d[i], d[best]] = [d[best], d[i]];
                        i = best;
                    } else break;
                }
            }
            return top;
        }
        peek() {
            return this.data[0];
        }
    }

    // Track per-prime active index sets and min/max heaps
    const primeInfo = new Map();
    let distinctPrimes = 0;

    const getPrimeEntry = (p) => {
        let entry = primeInfo.get(p);
        if (!entry) {
            entry = {
                indices: new Set(),
                minHeap: new Heap(true),
                maxHeap: new Heap(false),
                first: -1,
                last: -1
            };
            primeInfo.set(p, entry);
        }
        return entry;
    };

    // Synchronize a prime's [first + 1, last] interval on the segment tree
    const syncPrime = (p) => {
        const entry = primeInfo.get(p);
        // Remove previous range contribution if valid
        if (entry.first !== -1 && entry.first < entry.last) {
            updateRange(1, 1, n - 1, entry.first + 1, entry.last, -1);
        }

        if (entry.indices.size === 0) {
            entry.first = -1;
            entry.last = -1;
            return;
        }

        // Lazy-clean stale tops
        while (!entry.indices.has(entry.minHeap.peek())) entry.minHeap.pop();
        while (!entry.indices.has(entry.maxHeap.peek())) entry.maxHeap.pop();

        entry.first = entry.minHeap.peek();
        entry.last = entry.maxHeap.peek();

        // Add new range contribution if valid
        if (entry.first < entry.last) {
            updateRange(1, 1, n - 1, entry.first + 1, entry.last, 1);
        }
    };

    const addIndex = (p, idx) => {
        if (!isPrime[p]) return;
        const entry = getPrimeEntry(p);
        if (entry.indices.size === 0) distinctPrimes++;
        entry.indices.add(idx);
        entry.minHeap.push(idx);
        entry.maxHeap.push(idx);
        syncPrime(p);
    };

    const removeIndex = (p, idx) => {
        if (!isPrime[p]) return;
        const entry = primeInfo.get(p);
        entry.indices.delete(idx);
        if (entry.indices.size === 0) distinctPrimes--;
        syncPrime(p);
    };

    // 4. Initialize with initial array values
    for (let i = 0; i < n; i++) {
        if (isPrime[nums[i]]) {
            addIndex(nums[i], i);
        }
    }

    // 5. Process queries
    const ans = new Array(queries.length);
    for (let q = 0; q < queries.length; q++) {
        const [idx, val] = queries[q];
        const oldVal = nums[idx];

        if (oldVal !== val) {
            removeIndex(oldVal, idx);
            nums[idx] = val;
            addIndex(val, idx);
        }

        ans[q] = distinctPrimes + tree[1];
    }

    return ans;
};
