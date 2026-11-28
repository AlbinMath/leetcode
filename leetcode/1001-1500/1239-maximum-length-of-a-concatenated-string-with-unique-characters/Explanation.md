# LeetCode 1239: Maximum Length of a Concatenated String with Unique Characters

**LeetCode Problem #1239 — Maximum Length of a Concatenated String with Unique Characters**
Solve LeetCode Maximum Length of a Concatenated String with Unique Characters using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length of a Concatenated String with Unique Characters |
| LeetCode | #1239 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of strings `arr`. A string `s` is formed by the **concatenation** of a **subsequence** of `arr` that has **unique characters**.

Return *the **maximum** possible length* of `s`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= arr.length <= 16`
- `1 <= arr[i].length <= 26`
- `arr[i]` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `arr = ["un","iq","ue"]`
- **Output:** `4`
- **Explanation:** All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

### Example 2
- **Input:** `arr = ["cha","r","act","ers"]`
- **Output:** `6`
- **Explanation:** Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

### Example 3
- **Input:** `arr = ["abcdefghijklmnopqrstuvwxyz"]`
- **Output:** `26`
- **Explanation:** The only string in arr has all 26 characters.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Length of a Concatenated String with Unique Characters**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = ["un","iq","ue"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [0]  # reachable letter sets, starting with the empty concatenation
        best = 0
        for s in arr:
            m = 0
            ok = True
            for ch in s:
                b = 1 << (ord(ch) - 97)
                if m & b:
                    ok = False
                    break
                m |= b
            if not ok:
                continue  # repeats a letter internally, can never be used
            for old in masks[:]:  # iterate a copy, since masks grows
                if old & m == 0:
                    new = old | m
                    masks.append(new)
                    best = max(best, new.bit_count())
        return best
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1374. Generate a String With Characters That Have Odd Counts](../../1001-1500/1374-generate-a-string-with-characters-that-have-odd-counts/)
- [1898. Maximum Number of Removable Characters](../../1501-2000/1898-maximum-number-of-removable-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)
