# LeetCode 3569: Maximize Count of Distinct Primes After Split

**LeetCode Problem #3569 — Maximize Count of Distinct Primes After Split**
Solve LeetCode Maximize Count of Distinct Primes After Split using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Count of Distinct Primes After Split |
| LeetCode | #3569 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` having length `n` and a 2D integer array `queries` where `queries[i] = [idx, val]`.

For each query:

Update `nums[idx] = val`. 
 Choose an integer `k` with `1 <= k < n` to split the array into the non-empty prefix `nums[0..k-1]` and suffix `nums[k..n-1]` such that the sum of the counts of **distinct** prime values in each part is **maximum**.

Note: The changes made to the array in one query persist into the next query.

Return an array containing the result for each query, in the order they are given.

## Constraints
- `2 <= n == nums.length <= 5 * 10^4`
- `1 <= queries.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^5`
- `0 <= queries[i][0] < nums.length`
- `1 <= queries[i][1] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,1,2], queries = [[1,2],[3,3]]`
- **Output:** `[3,4]`
- **Explanation:** Initially `nums = [2, 1, 3, 1, 2]`. 
 After 1^st query, `nums = [2, 2, 3, 1, 2]`. Split `nums` into `[2]` and `[2, 3, 1, 2]`. `[2]` consists of 1 distinct prime and `[2, 3, 1, 2]` consists of 2 distinct primes. Hence, the answer for this query is `1 + 2 = 3`. 
 After 2^nd query, `nums = [2, 2, 3, 3, 2]`. Split `nums` into `[2, 2, 3]` and `[3, 2]` with an answer of `2 + 2 = 4`. 
 The output is `[3, 4]`.

### Example 2
- **Input:** `nums = [2,1,4], queries = [[0,1]]`
- **Output:** `[0]`
- **Explanation:** Initially `nums = [2, 1, 4]`. 
 After 1^st query, `nums = [1, 1, 4]`. There are no prime numbers in `nums`, hence the answer for this query is 0. 
 The output is `[0]`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximize Count of Distinct Primes After Split**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,1,2], queries = [[1,2],[3,3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4]`.
4. **Verification:** Initially `nums = [2, 1, 3, 1, 2]`. 
 After 1^st query, `nums = [2, 2, 3, 1, 2]`. Split `nums` into `[2]` and `[2, 3, 1, 2]`. `[2]` consists of 1 distinct prime and `[2, 3, 1, 2]` consists of 2 distinct primes. Hence, the answer for this query is `1 + 2 = 3`. 
 After 2^nd query, `nums = [2, 2, 3, 3, 2]`. Split `nums` into `[2, 2, 3]` and `[3, 2]` with an answer of `2 + 2 = 4`. 
 The output is `[3, 4]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
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
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/)
