# LeetCode 2900: Longest Unequal Adjacent Groups Subsequence I

**LeetCode Problem #2900 — Longest Unequal Adjacent Groups Subsequence I**
Solve LeetCode Longest Unequal Adjacent Groups Subsequence I using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Unequal Adjacent Groups Subsequence I |
| LeetCode | #2900 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string array `words` and a **binary** array `groups` both of length `n`.

A subsequence of `words` is **alternating** if for any two *consecutive* strings in the sequence, their corresponding elements at the *same* indices in `groups` are **different** (that is, there *cannot* be consecutive 0 or 1).

Your task is to select the **longest alternating** subsequence from `words`.

Return *the selected subsequence. If there are multiple answers, return **any** of them.*

**Note:** The elements in `words` are distinct.

## Constraints
- `1 <= n == words.length == groups.length <= 100`
- `1 <= words[i].length <= 10`
- `groups[i]` is either `0` or `1.`
- `words` consists of **distinct** strings.
- `words[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["e","a","b"], groups = [0,0,1]`
- **Output:** `["e","b"]`
- **Explanation:** A subsequence that can be selected is `["e","b"]` because `groups[0] != groups[2]`. Another subsequence that can be selected is `["a","b"]` because `groups[1] != groups[2]`. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is `2`.

### Example 2
- **Input:** `words = ["a","b","c","d"], groups = [1,0,1,1]`
- **Output:** `["a","b","c"]`
- **Explanation:** A subsequence that can be selected is `["a","b","c"]` because `groups[0] != groups[1]` and `groups[1] != groups[2]`. Another subsequence that can be selected is `["a","b","d"]` because `groups[0] != groups[1]` and `groups[1] != groups[3]`. It can be shown that the length of the longest subsequence of indices that satisfies the condition is `3`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Longest Unequal Adjacent Groups Subsequence I**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["e","a","b"], groups = [0,0,1]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["e","b"]`.
4. **Verification:** A subsequence that can be selected is `["e","b"]` because `groups[0] != groups[2]`. Another subsequence that can be selected is `["a","b"]` because `groups[1] != groups[2]`. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is `2`.

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
var getLongestSubsequence = function(words, groups) {
    let ans = [];

    ans.push(words[0]);

    for (let i = 1; i < words.length; i++) {
        if (groups[i] !== groups[i - 1]) {
            ans.push(words[i]);
        }
    }

    return ans;
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
- [516. Longest Palindromic Subsequence](../../0501-1000/0516-longest-palindromic-subsequence/)
- [521. Longest Uncommon Subsequence I](../../0501-1000/0521-longest-uncommon-subsequence-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/)
