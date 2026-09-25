/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} queries
 * @return {number[]}
 */
var resultArray = function(nums, k, queries) {
    const n = nums.length;

    // Segment tree size
    let size = 1;
    while (size < n) size <<= 1;

    // prod[node] = product of the whole segment modulo k
    const prod = new Int32Array(size * 2);

    // cnt[node * k + r] =
    // number of non-empty prefixes whose product % k == r
    const cnt = new Int32Array(size * 2 * k);

    // Empty segment has product 1 % k
    for (let i = 0; i < size; i++) {
        prod[size + i] = 1 % k;
    }

    // Build leaves
    for (let i = 0; i < n; i++) {
        const p = nums[i] % k;

        prod[size + i] = p;
        cnt[(size + i) * k + p] = 1;
    }

    // Build segment tree
    for (let node = size - 1; node >= 1; node--) {
        const left = node << 1;
        const right = left | 1;

        prod[node] = (prod[left] * prod[right]) % k;

        const base = node * k;
        const leftBase = left * k;
        const rightBase = right * k;

        // Prefixes completely inside the left child
        for (let r = 0; r < k; r++) {
            cnt[base + r] = cnt[leftBase + r];
        }

        // Prefixes that continue into the right child
        for (let r = 0; r < k; r++) {
            const c = cnt[rightBase + r];

            if (c !== 0) {
                const newR = (prod[left] * r) % k;
                cnt[base + newR] += c;
            }
        }
    }

    // Update one position
    function update(index, value) {
        let node = size + index;

        const p = value % k;

        prod[node] = p;

        const base = node * k;

        // Clear old counts
        for (let r = 0; r < k; r++) {
            cnt[base + r] = 0;
        }

        cnt[base + p] = 1;

        // Rebuild ancestors
        node >>= 1;

        while (node > 0) {
            const left = node << 1;
            const right = left | 1;

            prod[node] = (prod[left] * prod[right]) % k;

            const nodeBase = node * k;
            const leftBase = left * k;
            const rightBase = right * k;

            // Clear current node
            for (let r = 0; r < k; r++) {
                cnt[nodeBase + r] = cnt[leftBase + r];
            }

            // Add prefixes coming from right child
            for (let r = 0; r < k; r++) {
                const c = cnt[rightBase + r];

                if (c !== 0) {
                    const newR = (prod[left] * r) % k;
                    cnt[nodeBase + newR] += c;
                }
            }

            node >>= 1;
        }
    }

    // Query [start, n)
    function query(start) {
        let l = start + size;
        let r = n + size;

        // Left accumulator
        let leftProd = 1 % k;
        const leftCnt = new Int32Array(k);

        // Right accumulator
        let rightProd = 1 % k;
        const rightCnt = new Int32Array(k);

        while (l < r) {
            // Take left node
            if (l & 1) {
                const node = l;
                const nodeBase = node * k;

                // Existing prefixes remain unchanged
                const temp = new Int32Array(k);

                for (let x = 0; x < k; x++) {
                    temp[x] = leftCnt[x];
                }

                // Prefixes that continue into this node
                for (let x = 0; x < k; x++) {
                    const c = cnt[nodeBase + x];

                    if (c !== 0) {
                        const newR = (leftProd * x) % k;
                        temp[newR] += c;
                    }
                }

                for (let x = 0; x < k; x++) {
                    leftCnt[x] = temp[x];
                }

                leftProd = (leftProd * prod[node]) % k;
                l++;
            }

            // Take right node
            if (r & 1) {
                --r;

                const node = r;
                const nodeBase = node * k;

                const temp = new Int32Array(k);

                // Prefixes inside this node come first
                for (let x = 0; x < k; x++) {
                    temp[x] = cnt[nodeBase + x];
                }

                // Existing right-side prefixes come after this node
                for (let x = 0; x < k; x++) {
                    const c = rightCnt[x];

                    if (c !== 0) {
                        const newR = (prod[node] * x) % k;
                        temp[newR] += c;
                    }
                }

                for (let x = 0; x < k; x++) {
                    rightCnt[x] = temp[x];
                }

                rightProd = (prod[node] * rightProd) % k;
            }

            l >>= 1;
            r >>= 1;
        }

        // Combine left and right parts
        const answerCnt = new Int32Array(k);

        for (let x = 0; x < k; x++) {
            answerCnt[x] = leftCnt[x];
        }

        for (let x = 0; x < k; x++) {
            const c = rightCnt[x];

            if (c !== 0) {
                const newR = (leftProd * x) % k;
                answerCnt[newR] += c;
            }
        }

        return answerCnt;
    }

    const result = [];

    for (const [index, value, start, x] of queries) {
        // Permanent update
        update(index, value);

        // Count prefixes of nums[start...n-1]
        const counts = query(start);

        result.push(counts[x]);
    }

    return result;
};
