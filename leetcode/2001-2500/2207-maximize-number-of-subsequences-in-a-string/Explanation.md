# LeetCode 2207: Maximize Number of Subsequences in a String

**LeetCode Problem #2207 — Maximize Number of Subsequences in a String**
Solve LeetCode Maximize Number of Subsequences in a String using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Number of Subsequences in a String |
| LeetCode | #2207 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** string `text` and another **0-indexed** string `pattern` of length `2`, both of which consist of only lowercase English letters.

You can add **either** `pattern[0]` **or** `pattern[1]` anywhere in `text` **exactly once**. Note that the character can be added even at the beginning or at the end of `text`.

Return *the **maximum** number of times* `pattern` *can occur as a **subsequence** of the modified *`text`.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

## Constraints
- `1 <= text.length <= 10^5`
- `pattern.length == 2`
- `text` and `pattern` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `text = "abdcdbc", pattern = "ac"`
- **Output:** `4`
- **Explanation:** If we add pattern[0] = 'a' in between text[1] and text[2], we get "ab

### Example 2
- **Input:** `text = "aabb", pattern = "ab"`
- **Output:** `6`
- **Explanation:** Some of the strings which can be obtained from text and have 6 subsequences "ab" are "

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximize Number of Subsequences in a String**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "abdcdbc", pattern = "ac"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** If we add pattern[0] = 'a' in between text[1] and text[2], we get "ab

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
var maximumSubsequenceCount = function(text, pattern) {
    let countFirst = 0;
    let countSecond = 0;
    let subsequences = 0;

    for (let ch of text) {
        if (ch === pattern[1]) {
            subsequences += countFirst;
            countSecond++;
        }

        if (ch === pattern[0]) {
            countFirst++;
        }
    }
    return subsequences + Math.max(countFirst, countSecond);
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
- [1771. Maximize Palindrome Length From Subsequences](../../1501-2000/1771-maximize-palindrome-length-from-subsequences/)
- [1808. Maximize Number of Nice Divisors](../../1501-2000/1808-maximize-number-of-nice-divisors/)
- [2259. Remove Digit From Number to Maximize Result](../../2001-2500/2259-remove-digit-from-number-to-maximize-result/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/)
