# LeetCode 3848: Check Digitorial Permutation

**LeetCode Problem #3848 — Check Digitorial Permutation**
Solve LeetCode Check Digitorial Permutation using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Digitorial Permutation |
| LeetCode | #3848 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`.

A number is called **digitorial** if the sum of the **factorials** of its digits is **equal** to the number itself.

Determine whether **any permutation** of `n` (including the original order) forms a **digitorial** number.

Return `true` if such a **permutation** exists, otherwise return `false`.

**Note**:

The **factorial** of a non-negative integer `x`, denoted as `x!`, is the **product** of all positive integers **less than or equal** to `x`, and `0! = 1`. 
 A **permutation** is a rearrangement of all the digits of a number that does **not** start with zero. Any arrangement starting with zero is invalid.

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 145`
- **Output:** `true`
- **Explanation:** The number 145 itself is digitorial since `1! + 4! + 5! = 1 + 24 + 120 = 145`. Thus, the answer is `true`.

### Example 2
- **Input:** `n = 10`
- **Output:** `false`
- **Explanation:** ​​​​​​​ 

 10 is not digitorial since `1! + 0! = 2` is not equal to 10, and the permutation `"01"` is invalid because it starts with zero.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check Digitorial Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 145`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The number 145 itself is digitorial since `1! + 4! + 5! = 1 + 24 + 120 = 145`. Thus, the answer is `true`.

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
var isDigitorialPermutation = function(n) {
    const fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880];

    // Step 1: Calculate sum of digit factorials
    let temp = n;
    let sum = 0;

    while (temp > 0) {
        let digit = temp % 10;
        sum += fact[digit];
        temp = Math.floor(temp / 10);
    }

    // Step 2: Count digits of original number
    const freq1 = new Array(10).fill(0);
    const freq2 = new Array(10).fill(0);

    temp = n;

    while (temp > 0) {
        freq1[temp % 10]++;
        temp = Math.floor(temp / 10);
    }

    // Step 3: Count digits of factorial sum
    temp = sum;

    while (temp > 0) {
        freq2[temp % 10]++;
        temp = Math.floor(temp / 10);
    }

    // Step 4: Compare digit frequencies
    for (let i = 0; i < 10; i++) {
        if (freq1[i] !== freq2[i]) {
            return false;
        }
    }

    return true;
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
- [958. Check Completeness of a Binary Tree](../../0501-1000/0958-check-completeness-of-a-binary-tree/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)
- [1232. Check If It Is a Straight Line](../../1001-1500/1232-check-if-it-is-a-straight-line/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-digitorial-permutation/)
