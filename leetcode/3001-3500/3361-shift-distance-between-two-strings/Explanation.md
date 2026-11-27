# LeetCode 3361: Shift Distance Between Two Strings

**LeetCode Problem #3361 — Shift Distance Between Two Strings**
Solve LeetCode Shift Distance Between Two Strings using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shift Distance Between Two Strings |
| LeetCode | #3361 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s` and `t` of the same length, and two integer arrays `nextCost` and `previousCost`.

In one operation, you can pick any index `i` of `s`, and perform **either one** of the following actions:

Shift `s[i]` to the next letter in the alphabet. If `s[i] == 'z'`, you should replace it with `'a'`. This operation costs `nextCost[j]` where `j` is the index of `s[i]` in the alphabet. 
 Shift `s[i]` to the previous letter in the alphabet. If `s[i] == 'a'`, you should replace it with `'z'`. This operation costs `previousCost[j]` where `j` is the index of `s[i]` in the alphabet.

The **shift distance** is the **minimum** total cost of operations required to transform `s` into `t`.

Return the **shift distance** from `s` to `t`.

## Constraints
- `1 <= s.length == t.length <= 10^5`
- `s` and `t` consist only of lowercase English letters.
- `nextCost.length == previousCost.length == 26`
- `0 <= nextCost[i], previousCost[i] <= 10^9`

## Examples
### Example 1
- **Input:** `s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]`
- **Output:** `2`
- **Explanation:** We choose index `i = 0` and shift `s[0]` 25 times to the previous character for a total cost of 1. 
 We choose index `i = 1` and shift `s[1]` 25 times to the next character for a total cost of 0. 
 We choose index `i = 2` and shift `s[2]` 25 times to the previous character for a total cost of 1. 
 We choose index `i = 3` and shift `s[3]` 25 times to the next character for a total cost of 0.

### Example 2
- **Input:** `s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]`
- **Output:** `31`
- **Explanation:** We choose index `i = 0` and shift `s[0]` 9 times to the previous character for a total cost of 9. 
 We choose index `i = 1` and shift `s[1]` 10 times to the next character for a total cost of 10. 
 We choose index `i = 2` and shift `s[2]` 1 time to the previous character for a total cost of 1. 
 We choose index `i = 3` and shift `s[3]` 11 times to the next character for a total cost of 11.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shift Distance Between Two Strings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We choose index `i = 0` and shift `s[0]` 25 times to the previous character for a total cost of 1. 
 We choose index `i = 1` and shift `s[1]` 25 times to the next character for a total cost of 0. 
 We choose index `i = 2` and shift `s[2]` 25 times to the previous character for a total cost of 1. 
 We choose index `i = 3` and shift `s[3]` 25 times to the next character for a total cost of 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var shiftDistance = function(s, t, nextCost, previousCost) {
    const n = s.length;
    const nextPrefix = new Array(53).fill(0);
    const prevPrefix = new Array(53).fill(0);

    for (let i = 0; i < 52; i++) {
        nextPrefix[i + 1] = nextPrefix[i] + nextCost[i % 26];
        prevPrefix[i + 1] = prevPrefix[i] + previousCost[i % 26];
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const start = s.charCodeAt(i) - 97;
        const end = t.charCodeAt(i) - 97;
        const forward = (end - start + 26) % 26;
        const next = nextPrefix[start + forward] - nextPrefix[start];
        const backward = (start - end + 26) % 26;
        const prev = prevPrefix[start + 1 + 26] -
                     prevPrefix[start + 1 + 26 - backward];

        ans += Math.min(next, prev);
    }

    return ans;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1385-find-the-distance-value-between-two-arrays/)
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1360. Number of Days Between Two Dates](../../1001-1500/1360-number-of-days-between-two-dates/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shift-distance-between-two-strings/)
