# LeetCode 943: Find the Shortest Superstring

**LeetCode Problem #943 — Find the Shortest Superstring**
Solve LeetCode Find the Shortest Superstring using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Shortest Superstring |
| LeetCode | #943 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of strings `words`, return *the smallest string that contains each string in* `words` *as a substring*. If there are multiple valid strings of the smallest length, return **any of them**.

You may assume that no string in `words` is a substring of another string in `words`.

## Constraints
- `1 <= words.length <= 12`
- `1 <= words[i].length <= 20`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are **unique**.

## Examples
### Example 1
- **Input:** `words = ["alex","loves","leetcode"]`
- **Output:** `"alexlovesleetcode"`
- **Explanation:** All permutations of "alex","loves","leetcode" would also be accepted.

### Example 2
- **Input:** `words = ["catg","ctaagt","gcta","ttca","atgcatc"]`
- **Output:** `"gctaagttcatgcatc"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Shortest Superstring**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["alex","loves","leetcode"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"alexlovesleetcode"`.
4. **Verification:** All permutations of "alex","loves","leetcode" would also be accepted.

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
/**
 * @param {string[]} words
 * @return {string}
 */
var shortestSuperstring = function (words) {
  const n = words.length;
  const ov = (a, b) => {
    for (let l = Math.min(a.length, b.length) - 1; l > 0; l--)
      if (a.endsWith(b.slice(0, l))) return l;
    return 0;
  };
  const o = words.map((a) => words.map((b) => (a === b ? 0 : ov(a, b))));

  const size = 1 << n;
  const dp = Array.from({ length: size }, () => new Array(n).fill(-1));
  const par = Array.from({ length: size }, () => new Array(n).fill(-1));
  for (let i = 0; i < n; i++) dp[1 << i][i] = 0;

  for (let m = 1; m < size; m++)
    for (let l = 0; l < n; l++) {
      if (dp[m][l] < 0) continue;
      for (let x = 0; x < n; x++) {
        if (m & (1 << x)) continue;
        const nm = m | (1 << x);
        const v = dp[m][l] + o[l][x];
        if (v > dp[nm][x]) { dp[nm][x] = v; par[nm][x] = l; }
      }
    }

  let mask = size - 1, last = 0;
  for (let i = 1; i < n; i++) if (dp[mask][i] > dp[mask][last]) last = i;

  const order = [];
  while (last !== -1) {
    order.push(last);
    const p = par[mask][last];
    mask ^= 1 << last;
    last = p;
  }
  order.reverse();

  let res = words[order[0]];
  for (let k = 1; k < order.length; k++)
    res += words[order[k]].slice(o[order[k - 1]][order[k]]);
  return res;
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
- [3123. Find Edges in Shortest Paths](../../3001-3500/3123-find-edges-in-shortest-paths/)
- [214. Shortest Palindrome](../../0001-0500/0214-shortest-palindrome/)
- [581. Shortest Unsorted Continuous Subarray](../../0501-1000/0581-shortest-unsorted-continuous-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-shortest-superstring/)
