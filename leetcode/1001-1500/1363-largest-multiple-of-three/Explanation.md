# LeetCode 1363: Largest Multiple of Three

**LeetCode Problem #1363 — Largest Multiple of Three**
Solve LeetCode Largest Multiple of Three using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Multiple of Three |
| LeetCode | #1363 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of digits `digits`, return *the largest multiple of **three** that can be formed by concatenating some of the given digits in **any order***. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.

## Constraints
- `1 <= digits.length <= 10^4`
- `0 <= digits[i] <= 9`

## Examples
### Example 1
- **Input:** `digits = [8,1,9]`
- **Output:** `"981"`

### Example 2
- **Input:** `digits = [8,6,7,1,0]`
- **Output:** `"8760"`

### Example 3
- **Input:** `digits = [1]`
- **Output:** `""`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Largest Multiple of Three**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `digits = [8,1,9]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"981"`.

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
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()  # ascending, so the first matches are the smallest
        total = sum(digits)
        r = total % 3

        def remove(rem: int, count: int) -> bool:
            idxs = [i for i, d in enumerate(digits) if d % 3 == rem][:count]
            if len(idxs) < count:
                return False
            for i in reversed(idxs):
                digits.pop(i)
            return True

        if r == 1:
            if not remove(1, 1):
                remove(2, 2)
        elif r == 2:
            if not remove(2, 1):
                remove(1, 2)

        if not digits:
            return ""
        if digits[-1] == 0:
            return "0"
        return ''.join(map(str, reversed(digits)))
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
- [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](../../1501-2000/1509-minimum-difference-between-largest-and-smallest-value-in-three-moves/)
- [1354. Construct Target Array With Multiple Sums](../../1001-1500/1354-construct-target-array-with-multiple-sums/)
- [2248. Intersection of Multiple Arrays](../../2001-2500/2248-intersection-of-multiple-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-multiple-of-three/)
