# LeetCode 3752: Lexicographically Smallest Negated Permutation that Sums to Target

**LeetCode Problem #3752 — Lexicographically Smallest Negated Permutation that Sums to Target**
Solve LeetCode Lexicographically Smallest Negated Permutation that Sums to Target using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest Negated Permutation that Sums to Target |
| LeetCode | #3752 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n` and an integer `target`.

Return the ** lexicographically smallest ** array of integers of size `n` such that:

The **sum** of its elements equals `target`. 
 The **absolute values** of its elements form a **permutation** of size `n`.

If no such array exists, return an empty array.

A **permutation** of size `n` is a rearrangement of integers `1, 2, ..., n`.

## Constraints
- `1 <= n <= 10^5`
- `-10^10 <= target <= 10^10`

## Examples
### Example 1
- **Input:** `n = 3, target = 0`
- **Output:** `[-3,1,2]`
- **Explanation:** The arrays that sum to 0 and whose absolute values form a permutation of size 3 are: 

 
 `[-3, 1, 2]` 
 `[-3, 2, 1]` 
 `[-2, -1, 3]` 
 `[-2, 3, -1]` 
 `[-1, -2, 3]` 
 `[-1, 3, -2]` 
 `[1, -3, 2]` 
 `[1, 2, -3]` 
 `[2, -3, 1]` 
 `[2, 1, -3]` 
 `[3, -2, -1]` 
 `[3, -1, -2]` 
 

 The lexicographically smallest one is `[-3, 1, 2]`.

### Example 2
- **Input:** `n = 1, target = 10000000000`
- **Output:** `[]`
- **Explanation:** There are no arrays that sum to 10000000000 and whose absolute values form a permutation of size 1. Therefore, the answer is `[]`.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest Negated Permutation that Sums to Target**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, target = 0`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[-3,1,2]`.
4. **Verification:** The arrays that sum to 0 and whose absolute values form a permutation of size 3 are: 

 
 `[-3, 1, 2]` 
 `[-3, 2, 1]` 
 `[-2, -1, 3]` 
 `[-2, 3, -1]` 
 `[-1, -2, 3]` 
 `[-1, 3, -2]` 
 `[1, -3, 2]` 
 `[1, 2, -3]` 
 `[2, -3, 1]` 
 `[2, 1, -3]` 
 `[3, -2, -1]` 
 `[3, -1, -2]` 
 

 The lexicographically smallest one is `[-3, 1, 2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var lexSmallestNegatedPerm = function(n, target) {
    const total = (n * (n + 1)) / 2;

    if (target < -total || target > total) {
        return [];
    }

    if ((total - target) % 2 !== 0) {
        return [];
    }

    let remaining = (total - target) / 2;

    const negative = [];
    const positive = [];

    for (let i = n; i >= 1; i--) {
        if (remaining >= i) {
            negative.push(-i);
            remaining -= i;
        } else {
            positive.push(i);
        }
    }

    positive.reverse();

    return [...negative, ...positive];
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3720. Lexicographically Smallest Permutation Greater Than Target](../../3501-4000/3720-lexicographically-smallest-permutation-greater-than-target/)
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../../3501-4000/3734-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/)
