# LeetCode 1621: Number of Sets of K Non-Overlapping Line Segments

**LeetCode Problem #1621 — Number of Sets of K Non-Overlapping Line Segments**
Solve LeetCode Number of Sets of K Non-Overlapping Line Segments using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Sets of K Non-Overlapping Line Segments |
| LeetCode | #1621 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given `n` points on a 1-D plane, where the `i^th` point (from `0` to `n-1`) is at `x = i`, find the number of ways we can draw **exactly** `k` **non-overlapping** line segments such that each segment covers two or more points. The endpoints of each segment must have **integral coordinates**. The `k` line segments **do not** have to cover all `n` points, and they are **allowed** to share endpoints.

Return *the number of ways we can draw *`k`* non-overlapping line segments**.* Since this number can be huge, return it **modulo** `10^9 + 7`.

## Constraints
- `2 <= n <= 1000`
- `1 <= k <= n-1`

## Examples
### Example 1
- **Input:** `n = 4, k = 2`
- **Output:** `5`
- **Explanation:** The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

### Example 2
- **Input:** `n = 3, k = 1`
- **Output:** `3`
- **Explanation:** The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.

### Example 3
- **Input:** `n = 30, k = 7`
- **Output:** `796297179`
- **Explanation:** The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 10^9 + 7 gives us 796297179.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses an optimized **DP with prefix sums**.

1. `dp[j]` = number of ways to choose `j` segments using points processed so far.
2. `prefix[j]` accumulates the sum of `dp[j-1]` values, enabling efficient transitions.
3. For each new point `i` (from 1 to n-1), update the prefix sums and then use them to update `dp[j]`.

Time complexity is $O(N \times K)$ and space complexity is $O(K)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, k = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numberOfSets = function(n, k) {
    const MOD = 1000000007;

    // dp[j] = number of ways to choose j non-overlapping segments
    const dp = Array(k + 1).fill(0);
    dp[0] = 1;

    // prefix[j] stores cumulative dp[j]
    const prefix = Array(k + 1).fill(0);

    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= k; j++) {
            prefix[j] = (prefix[j] + dp[j - 1]) % MOD;
        }

        for (let j = 1; j <= k; j++) {
            dp[j] = (dp[j] + prefix[j]) % MOD;
        }
    }

    return dp[k];
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1520. Maximum Number of Non-Overlapping Substrings](../../1501-2000/1520-maximum-number-of-non-overlapping-substrings/)
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)
- [2472. Maximum Number of Non-overlapping Palindrome Substrings](../../2001-2500/2472-maximum-number-of-non-overlapping-palindrome-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)
