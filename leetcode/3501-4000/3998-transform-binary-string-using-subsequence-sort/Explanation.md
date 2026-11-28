# LeetCode 3998: Transform Binary String Using Subsequence Sort

**LeetCode Problem #3998 — Transform Binary String Using Subsequence Sort**
Solve LeetCode Transform Binary String Using Subsequence Sort using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Transform Binary String Using Subsequence Sort |
| LeetCode | #3998 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `s`.

You are also given an array of strings `strs`, where each `strs[i]` has the **same** length as `s` and consists of characters `'0'`, `'1'`, and `'?'`. Each `'?'` can be replaced by either `'0'` or `'1'`.

You may perform the following operation any number of times (including zero):

Choose any subsequence `sub` of `s`. 
 Sort `sub` in **non-decreasing** order. 
 Replace the chosen **subsequence** in `s` with the sorted `sub`, keeping all other characters unchanged.

Return a boolean array `ans`, where `ans[i]` is `true` if it's possible to replace all `'?'` in `strs[i]` with `'0'` or `'1'` and transform `s` into the resulting string using the allowed operation above, otherwise return `false`.

## Constraints
- `1 <= n == s.length <= 2000`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= strs.length <= 2000`
- `strs[i].length == n`
- `strs[i]` is either `'0'`, `'1'`, or `'?'`​​​​​​​.

## Examples
### Example 1
- **Input:** `s = "101", strs = ["1?1","0?1","0?0"]`
- **Output:** `[true,true,false]`
- **Explanation:** `i` 
 `strs[i]` 
 Replacement 
 Result `strs[i]` 
 Operation(s) 
 Result 
 
 
 0 
 `"1?1"` 
 `? &rarr; 0` 
 `"101"` 
 Matches `s`. 
 `true` 
 
 
 1 
 `"0?1"` 
 `? &rarr; 1` 
 `"011"` 
 Select the subsequence at indices `[0..2]` of `s` &rarr; `"101"`. 
 Sort `"101"` to get `"011" = strs[i]`. 
 `true` 
 
 
 2 
 `"0?0"` 
 `? &rarr; 0` or `1` 
 `"000"` or `"010"` 
 Not feasible. 
 `false` 
 
 
 

 Thus, `ans = [true, true, false]`.

### Example 2
- **Input:** `s = "1100", strs = ["0011","11?1","1?1?"]`
- **Output:** `[true,false,true]`
- **Explanation:** `i` 
 `strs[i]` 
 Replacement 
 Result `strs[i]` 
 Operation(s) 
 Result 
 
 
 0 
 `"0011"` 
 - 
 `"0011"` 
 Select the subsequence at indices `[0..3]` of `s` &rarr; `"1100"`. 
 Sort `"1100"` to get `"0011" = strs[i]`. 
 `true` 
 
 
 1 
 `"11?1"` 
 `? &rarr; 0` 
 `"1101"` 
 Not feasible. 
 `false` 
 
 
 2 
 `"1?1?"` 
 First `? &rarr; 0` 
 Second `? &rarr; 0` 
 `"1010"` 
 Select the subsequence at indices `[1, 2]` of `s` &rarr; `"10"`. 
 Sort `"10"` to get `"01"`, so `s = "1 01 0"`. 
 `true` 
 
 
 

 Thus, `ans = [true, false, true]`.

### Example 3
- **Input:** `s = "1010", strs = ["0011"]`
- **Output:** `[true]`
- **Explanation:** `i` 
 `strs[i]` 
 Replacement 
 Result `strs[i]` 
 Operation(s) 
 Result 
 
 
 0 
 `"0011"` 
 - 
 `"0011"` 
 Select the subsequence at indices `[0, 2, 3]` of `s` &rarr; `"110"`. 
 Sort `"110"` to get `"011"`, so `s = "0 0 11" = strs[i]`. 
 `true` 
 
 
 

 Thus, `ans = [true]`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Transform Binary String Using Subsequence Sort**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "101", strs = ["1?1","0?1","0?0"]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,true,false]`.
4. **Verification:** `i` 
 `strs[i]` 
 Replacement 
 Result `strs[i]` 
 Operation(s) 
 Result 
 
 
 0 
 `"1?1"` 
 `? &rarr; 0` 
 `"101"` 
 Matches `s`. 
 `true` 
 
 
 1 
 `"0?1"` 
 `? &rarr; 1` 
 `"011"` 
 Select the subsequence at indices `[0..2]` of `s` &rarr; `"101"`. 
 Sort `"101"` to get `"011" = strs[i]`. 
 `true` 
 
 
 2 
 `"0?0"` 
 `? &rarr; 0` or `1` 
 `"000"` or `"010"` 
 Not feasible. 
 `false` 
 
 
 

 Thus, `ans = [true, true, false]`.

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
var transformStr = function(s, strs) {
    const n = s.length;

    let totalOnes = 0;

    for (let i = 0; i < n; i++) {
        if (s[i] === '1') totalOnes++;
    }

    const ans = [];

    for (const pattern of strs) {
        let fixedOnes = 0;
        let questionMarks = 0;

        for (let i = 0; i < n; i++) {
            if (pattern[i] === '1') {
                fixedOnes++;
            } else if (pattern[i] === '?') {
                questionMarks++;
            }
        }

        const needed = totalOnes - fixedOnes;

        if (needed < 0 || needed > questionMarks) {
            ans.push(false);
            continue;
        }

        let remaining = needed;
        let sourceOnes = 0;
        let targetOnes = 0;
        let possible = true;

        const wildcardOnes = new Array(n).fill(false);

        for (let i = n - 1; i >= 0 && remaining > 0; i--) {
            if (pattern[i] === '?') {
                wildcardOnes[i] = true;
                remaining--;
            }
        }

        for (let i = 0; i < n; i++) {
            if (s[i] === '1') sourceOnes++;

            if (pattern[i] === '1' || wildcardOnes[i]) {
                targetOnes++;
            }

            if (targetOnes > sourceOnes) {
                possible = false;
                break;
            }
        }

        ans.push(possible);
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
- [3980. Minimum Operations to Transform Binary String](../../3501-4000/3980-minimum-operations-to-transform-binary-string/)
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)
- [761. Special Binary String](../../0501-1000/0761-special-binary-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/)
