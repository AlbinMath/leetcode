# LeetCode 3901: Good Subsequence Queries

**LeetCode Problem #3901 — Good Subsequence Queries**
Solve LeetCode Good Subsequence Queries using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Good Subsequence Queries |
| LeetCode | #3901 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `p`.

A **non-empty subsequence ** of `nums` is called **good** if:

Its length is **strictly less** than `n`. 
 The **greatest common divisor (GCD)** of its elements is **exactly** `p`.

You are also given a 2D integer array `queries` of length `q`, where each `queries[i] = [ind_i, val_i]` indicates that you should update `nums[ind_i]` to `val_i`.

After each query, determine whether there exists **any good subsequence** in the current array.

Return the **number** of queries for which a **good subsequence** exists.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

## Constraints
- `2 <= n == nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 5 * 10^4`
- `1 <= queries.length <= 5 * 10^4`
- `queries[i] = [ind_i, val_i]`
- `1 <= val_i, p <= 5 * 10^4`
- `0 <= ind_i <= n - 1`

## Examples
### Example 1
- **Input:** `nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]`
- **Output:** `1`
- **Explanation:** i 
 `[ind_i, val_i]` 
 Operation 
 Updated `nums` 
 Any good Subsequence 
 
 
 
 
 0 
 `[0, 3]` 
 Update `nums[0]` to `3` 
 `[3, 8, 12, 16]` 
 No, as no subsequence has GCD exactly `p = 2` 
 
 
 1 
 `[2, 6]` 
 Update `nums[2]` to `6` 
 `[3, 8, 6, 16]` 
 Yes, subsequence `[8, 6]` has GCD exactly `p = 2` 
 
 
 

 Thus, the answer is 1.

### Example 2
- **Input:** `nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]`
- **Output:** `2`
- **Explanation:** i 
 `[ind_i, val_i]` 
 Operation 
 Updated `nums` 
 Any good Subsequence 
 
 
 
 
 0 
 `[0, 6]` 
 Update `nums[0]` to `6` 
 `[6, 5, 7, 8]` 
 No, as no subsequence has GCD exactly `p = 3` 
 
 
 1 
 `[1, 9]` 
 Update `nums[1]` to `9` 
 `[6, 9, 7, 8]` 
 Yes, subsequence `[6, 9]` has GCD exactly `p = 3` 
 
 
 2 
 `[2, 3]` 
 Update `nums[2]` to `3` 
 `[6, 9, 3, 8]` 
 Yes, subsequence `[6, 9, 3]` has GCD exactly `p = 3` 
 
 
 

 Thus, the answer is 2.

### Example 3
- **Input:** `nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]`
- **Output:** `0`
- **Explanation:** i 
 `[ind_i, val_i]` 
 Operation 
 Updated `nums` 
 Any good Subsequence 
 
 
 
 
 0 
 `[1, 4]` 
 Update `nums[1]` to `4` 
 `[5, 4, 9]` 
 No, as no subsequence has GCD exactly `p = 2` 
 
 
 1 
 `[2, 8]` 
 Update `nums[2]` to `8` 
 `[5, 4, 8]` 
 No, as no subsequence has GCD exactly `p = 2` 
 
 
 

 Thus, the answer is 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Good Subsequence Queries**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** i 
 `[ind_i, val_i]` 
 Operation 
 Updated `nums` 
 Any good Subsequence 
 
 
 
 
 0 
 `[0, 3]` 
 Update `nums[0]` to `3` 
 `[3, 8, 12, 16]` 
 No, as no subsequence has GCD exactly `p = 2` 
 
 
 1 
 `[2, 6]` 
 Update `nums[2]` to `6` 
 `[3, 8, 6, 16]` 
 Yes, subsequence `[8, 6]` has GCD exactly `p = 2` 
 
 
 

 Thus, the answer is 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
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
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [334. Increasing Triplet Subsequence](../../0001-0500/0334-increasing-triplet-subsequence/)
- [376. Wiggle Subsequence](../../0001-0500/0376-wiggle-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/good-subsequence-queries/)
