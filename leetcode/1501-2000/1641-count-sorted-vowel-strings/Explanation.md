# LeetCode 1641: Count Sorted Vowel Strings

**LeetCode Problem #1641 — Count Sorted Vowel Strings**
Solve LeetCode Count Sorted Vowel Strings using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Sorted Vowel Strings |
| LeetCode | #1641 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer `n`, return *the number of strings of length *`n`* that consist only of vowels (*`a`*, *`e`*, *`i`*, *`o`*, *`u`*) and are **lexicographically sorted**.*

A string `s` is **lexicographically sorted** if for all valid `i`, `s[i]` is the same as or comes before `s[i+1]` in the alphabet.

## Constraints
- `1 <= n <= 50`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `5`
- **Explanation:** The 5 sorted strings that consist of vowels only are `["a","e","i","o","u"].`

### Example 2
- **Input:** `n = 2`
- **Output:** `15`
- **Explanation:** The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

### Example 3
- **Input:** `n = 33`
- **Output:** `66045`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count Sorted Vowel Strings**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The 5 sorted strings that consist of vowels only are `["a","e","i","o","u"].`

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
var countVowelStrings = function(n) {
    let dp = [1, 1, 1, 1, 1];

    for (let i = 2; i <= n; i++) {
        for (let j = 3; j >= 0; j--) {
            dp[j] += dp[j + 1];
        }
    }

    return dp.reduce((sum, count) => sum + count, 0);
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
- [2586. Count the Number of Vowel Strings in Range](../../2501-3000/2586-count-the-number-of-vowel-strings-in-range/)
- [1351. Count Negative Numbers in a Sorted Matrix](../../1001-1500/1351-count-negative-numbers-in-a-sorted-matrix/)
- [1684. Count the Number of Consistent Strings](../../1501-2000/1684-count-the-number-of-consistent-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-sorted-vowel-strings/)
