# LeetCode 3458: Select K Disjoint Special Substrings

**LeetCode Problem #3458 — Select K Disjoint Special Substrings**
Solve LeetCode Select K Disjoint Special Substrings using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Select K Disjoint Special Substrings |
| LeetCode | #3458 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` of length `n` and an integer `k`, determine whether it is possible to select `k` disjoint **special substrings**.

A **special substring** is a substring where:

Any character present inside the substring should not appear outside it in the string. 
 The substring is not the entire string `s`.

**Note** that all `k` substrings must be disjoint, meaning they cannot overlap.

Return `true` if it is possible to select `k` such disjoint special substrings; otherwise, return `false`.

## Constraints
- `2 <= n == s.length <= 5 * 10^4`
- `0 <= k <= 26`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcdbaefab", k = 2`
- **Output:** `true`
- **Explanation:** We can select two disjoint special substrings: `"cd"` and `"ef"`. 
 `"cd"` contains the characters `'c'` and `'d'`, which do not appear elsewhere in `s`. 
 `"ef"` contains the characters `'e'` and `'f'`, which do not appear elsewhere in `s`.

### Example 2
- **Input:** `s = "cdefdc", k = 3`
- **Output:** `false`
- **Explanation:** There can be at most 2 disjoint special substrings: `"e"` and `"f"`. Since `k = 3`, the output is `false`.

### Example 3
- **Input:** `s = "abeabe", k = 0`
- **Output:** `true`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Select K Disjoint Special Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcdbaefab", k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can select two disjoint special substrings: `"cd"` and `"ef"`. 
 `"cd"` contains the characters `'c'` and `'d'`, which do not appear elsewhere in `s`. 
 `"ef"` contains the characters `'e'` and `'f'`, which do not appear elsewhere in `s`.

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
var maxSubstringLength = function(s, k) {
    if (k === 0) return true;

    const n = s.length;

    const first = new Array(26).fill(n);
    const last = new Array(26).fill(-1);
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;

        first[c] = Math.min(first[c], i);
        last[c] = i;
    }

    const intervals = [];
    for (let c = 0; c < 26; c++) {
        if (last[c] === -1) continue;

        const start = first[c];
        let end = last[c];
        let valid = true;
        for (let i = start; i <= end; i++) {
            const x = s.charCodeAt(i) - 97;

            if (first[x] < start) {
                valid = false;
                break;
            }

            end = Math.max(end, last[x]);
        }
        if (valid && !(start === 0 && end === n - 1)) {
            intervals.push([start, end]);
        }
    }
    intervals.sort((a, b) => a[1] - b[1]);
    let count = 0;
    let previousEnd = -1;

    for (const [start, end] of intervals) {
        if (start > previousEnd) {
            count++;
            previousEnd = end;

            if (count >= k) return true;
        }
    }

    return false;
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
- [3077. Maximum Strength of K Disjoint Subarrays](../../3001-3500/3077-maximum-strength-of-k-disjoint-subarrays/)
- [2522. Partition String Into Substrings With Values at Most K](../../2501-3000/2522-partition-string-into-substrings-with-values-at-most-k/)
- [3258. Count Substrings That Satisfy K-Constraint I](../../3001-3500/3258-count-substrings-that-satisfy-k-constraint-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/select-k-disjoint-special-substrings/)
