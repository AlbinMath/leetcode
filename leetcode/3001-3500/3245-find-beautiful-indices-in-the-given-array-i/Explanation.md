# LeetCode 3006: Find Beautiful Indices in the Given Array I

**LeetCode Problem #3006 — Find Beautiful Indices in the Given Array I**
Solve LeetCode Find Beautiful Indices in the Given Array I using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Beautiful Indices in the Given Array I |
| LeetCode | #3006 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `s`, a string `a`, a string `b`, and an integer `k`.

An index `i` is **beautiful** if:

`0 <= i <= s.length - a.length` 
 `s[i..(i + a.length - 1)] == a` 
 There exists an index `j` such that:
 
 `0 <= j <= s.length - b.length` 
 `s[j..(j + b.length - 1)] == b` 
 `|j - i| <= k`

Return *the array that contains beautiful indices in **sorted order from smallest to largest***.

## Constraints
- `1 <= k <= s.length <= 10^5`
- `1 <= a.length, b.length <= 10`
- `s`, `a`, and `b` contain only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15`
- **Output:** `[16,33]`
- **Explanation:** There are 2 beautiful indices: [16,33].
- The index 16 is beautiful as s[16..17] == "my" and there exists an index 4 with s[4..11] == "squirrel" and |16 - 4| <= 15.
- The index 33 is beautiful as s[33..34] == "my" and there exists an index 18 with s[18..25] == "squirrel" and |33 - 18| <= 15.
Thus we return [16,33] as the result.

### Example 2
- **Input:** `s = "abcd", a = "a", b = "a", k = 4`
- **Output:** `[0]`
- **Explanation:** There is 1 beautiful index: [0].
- The index 0 is beautiful as s[0..0] == "a" and there exists an index 0 with s[0..0] == "a" and |0 - 0| <= 4.
Thus we return [0] as the result.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Beautiful Indices in the Given Array I**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[16,33]`.
4. **Verification:** There are 2 beautiful indices: [16,33].
- The index 16 is beautiful as s[16..17] == "my" and there exists an index 4 with s[4..11] == "squirrel" and |16 - 4| <= 15.
- The index 33 is beautiful as s[33..34] == "my" and there exists an index 18 with s[18..25] == "squirrel" and |33 - 18| <= 15.
Thus we return [16,33] as the result.

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
from bisect import bisect_left
from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(p: str) -> List[int]:
            m = len(p)
            return [i for i in range(len(s) - m + 1) if s[i:i + m] == p]

        A = occurrences(a)
        B = occurrences(b)

        res = []
        for i in A:
            # smallest j in B with j >= i - k
            pos = bisect_left(B, i - k)
            if pos < len(B) and B[pos] <= i + k:
                res.append(i)
        return res
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
- [3008. Find Beautiful Indices in the Given Array II](../../3001-3500/3303-find-beautiful-indices-in-the-given-array-ii/)
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2210-find-target-indices-after-sorting-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/)
