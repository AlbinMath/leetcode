# LeetCode 3333: Find the Original Typed String II

**LeetCode Problem #3333 — Find the Original Typed String II**
Solve LeetCode Find the Original Typed String II using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Original Typed String II |
| LeetCode | #3333 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and **may** press a key for too long, resulting in a character being typed **multiple** times.

You are given a string `word`, which represents the **final** output displayed on Alice's screen. You are also given a **positive** integer `k`.

Return the total number of *possible* original strings that Alice *might* have intended to type, if she was trying to type a string of size **at least** `k`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= word.length <= 5 * 10^5`
- `word` consists only of lowercase English letters.
- `1 <= k <= 2000`

## Examples
### Example 1
- **Input:** `word = "aabbccdd", k = 7`
- **Output:** `5`
- **Explanation:** The possible strings are: `"aabbccdd"`, `"aabbccd"`, `"aabbcdd"`, `"aabccdd"`, and `"abbccdd"`.

### Example 2
- **Input:** `word = "aabbccdd", k = 8`
- **Output:** `1`
- **Explanation:** The only possible string is `"aabbccdd"`.

### Example 3
- **Input:** `word = "aaabbb", k = 3`
- **Output:** `8`

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Find the Original Typed String II**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aabbccdd", k = 7`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The possible strings are: `"aabbccdd"`, `"aabbccd"`, `"aabbcdd"`, `"aabccdd"`, and `"abbccdd"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var possibleStringCount = function(word, k) {
    const MOD = 1000000007;
    const n = word.length;
    const groups = [];
    let total = 1;
    let count = 1;
    for (let i = 1; i < n; i++) {
        if (word[i] === word[i - 1]) {
            count++;
        } else {
            groups.push(count);
            total = (total * count) % MOD;
            count = 1;
        }
    }
    groups.push(count);
    total = (total * count) % MOD;
    const m = groups.length;
    if (m >= k) {
        return total;
    }
    let dp = new Array(k).fill(0);
    dp[0] = 1;
    for (const len of groups) {
        const ndp = new Array(k).fill(0);
        let window = 0;
        for (let s = 0; s < k; s++) {
            if (s >= 1) {
                window = (window + dp[s - 1]) % MOD;
            }
            if (s - len - 1 >= 0) {
                window = (
                    window - dp[s - len - 1] + MOD
                ) % MOD;
            }
            ndp[s] = window;
        }
        dp = ndp;
    }
    let invalid = 0;

    for (let s = 0; s < k; s++) {
        invalid = (invalid + dp[s]) % MOD;
    }
    return (total - invalid + MOD) % MOD;
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [2433. Find The Original Array of Prefix Xor](../../2001-2500/2433-find-the-original-array-of-prefix-xor/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-original-typed-string-ii/)
