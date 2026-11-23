# LeetCode 3525: Find X Value of Array II

**LeetCode Problem #3525 — Find X Value of Array II**
Solve LeetCode Find X Value of Array II using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find X Value of Array II |
| LeetCode | #3525 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of **positive** integers `nums` and a **positive** integer `k`. You are also given a 2D array `queries`, where `queries[i] = [index_i, value_i, start_i, x_i]`.

You are allowed to perform an operation **once** on `nums`, where you can remove any **suffix** from `nums` such that `nums` remains **non-empty**.

The **x-value** of `nums` **for a given** `x` is defined as the number of ways to perform this operation so that the **product** of the remaining elements leaves a *remainder* of `x` **modulo** `k`.

For each query in `queries` you need to determine the **x-value** of `nums` for `x_i` after performing the following actions:

Update `nums[index_i]` to `value_i`. Only this step persists for the rest of the queries. 
 **Remove** the prefix `nums[0..(start_i - 1)]` (where `nums[0..(-1)]` will be used to represent the **empty** prefix).

Return an array `result` of size `queries.length` where `result[i]` is the answer for the `i^th` query.

A **prefix** of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A **suffix** of an array is a subarray that starts at any point within the array and extends to the end of the array.

**Note** that the prefix and suffix to be chosen for the operation can be **empty**.

**Note** that x-value has a *different* definition in this version.

## Constraints
- `1 <= nums[i] <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= k <= 5`
- `1 <= queries.length <= 2 * 10^4`
- `queries[i] == [index_i, value_i, start_i, x_i]`
- `0 <= index_i <= nums.length - 1`
- `1 <= value_i <= 10^9`
- `0 <= start_i <= nums.length - 1`
- `0 <= x_i <= k - 1`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]`
- **Output:** `[2,2,2]`
- **Explanation:** For query 0, `nums` becomes `[1, 2, 2, 4, 5]`, and the empty prefix

### Example 2
- **Input:** `nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]`
- **Output:** `[1,0]`
- **Explanation:** For query 0, `nums` becomes `[2, 2, 4, 8, 16, 32]`. The only possible operation is:

 
 Remove the suffix `[2, 4, 8, 16, 32]`. 
 
 
 For query 1, `nums` becomes `[2, 2, 4, 8, 16, 32]`. There is no possible way to perform the operation.

### Example 3
- **Input:** `nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]`
- **Output:** `[5]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
Because updates are persistent and there can be many queries, calculating the answers iteratively would be too slow. The code uses a **Segment Tree** to answer queries and handle updates efficiently.

1. **Segment Tree Structure**:
   - `prod` stores the product modulo `k` of all elements within a segment.
   - `cnt` is flattened 2D array. For each segment node, it stores an array of size `k` where `cnt[node * k + r]` is the number of valid prefixes (relative to the segment's start) whose product modulo `k` is `r`.
2. **Building the Tree**:
   - It initializes the leaves with individual array elements.
   - For internal nodes, it computes the `prod` as the product of its left and right children modulo `k`.
   - The `cnt` for an internal node is formed by:
     - Taking all prefixes from the left child (as they are also prefixes of the parent segment).
     - Taking prefixes from the right child, but multiplying their products by the total product of the left child, because a prefix extending into the right child must include all of the left child.
3. **Updating (`update` function)**:
   - When an element is updated, it updates the corresponding leaf node's `prod` and `cnt`.
   - It then traverses up the tree to the root, recalculating `prod` and `cnt` for every ancestor just like during the build phase.
4. **Querying (`query` function)**:
   - To find the counts for a subarray starting at `start` and ending at `n-1`, it queries the segment tree for the range `[start, n)`.
   - It accumulates the results from left to right. Just like building nodes, it keeps a running `leftProd` and a `leftCnt` array, merging them with the relevant nodes from the segment tree to compute the final counts of prefix products for the requested range.
5. For each query, it performs the update, calls the query function, and pushes the count for the requested remainder `x` into the `result` array.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,2,2]`.
4. **Verification:** For query 0, `nums` becomes `[1, 2, 2, 4, 5]`, and the empty prefix

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
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
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3524. Find X Value of Array I](../../3501-4000/3831-find-x-value-of-array-i/)
- [2562. Find the Array Concatenation Value](../../2501-3000/2698-find-the-array-concatenation-value/)
- [3287. Find the Maximum Sequence Value of Array](../../3501-4000/3575-find-the-maximum-sequence-value-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-x-value-of-array-ii/)
