# LeetCode 4059: Lexicographically Largest Power Array

**LeetCode Problem #4059 — Lexicographically Largest Power Array**
Solve LeetCode Lexicographically Largest Power Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Largest Power Array |
| LeetCode | #4059 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`. You may rearrange its elements to form any permutation `perm`.

Define an array `power` of length 15. For each `0 <= i < 15`, `power[i]` is the largest integer `j`, where `0 <= j <= n`, such that the first `j` elements of `perm` all have the `(14 - i)^th` bit set .

Bit positions are indexed from right to left, starting with the `0^th` bit.

Return the lexicographically largest possible `power` array.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] < 2^15`

## Examples
### Example 1
- **Input:** `nums = [7,5]`
- **Output:** `[0,0,0,0,0,0,0,0,0,0,0,0,2,1,2]`
- **Explanation:** Choose `perm = [7, 5]`. 

 
 Both elements have bit 2 set, so `power[12] = 2`. 
 The first element has bit 1 set, but the second does not, so `power[13] = 1`. 
 Both elements have bit 0 set, so `power[14] = 2`. 
 

 All higher bits are unset in the first element, so the remaining entries are 0.

### Example 2
- **Input:** `nums = [3,1,7]`
- **Output:** `[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3]`
- **Explanation:** Choose `perm = [7, 3, 1]`. 

 
 The first element has bit 2 set, but the second does not, so `power[12] = 1`. 
 The first two elements have bit 1 set, but the third does not, so `power[13] = 2`. 
 All three elements have bit 0 set, so `power[14] = 3`. 
 

 All higher bits are unset in the first element, so the remaining entries are 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Lexicographically Largest Power Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [7,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,0,0,0,0,0,0,0,0,0,0,0,2,1,2]`.
4. **Verification:** Choose `perm = [7, 5]`. 

 
 Both elements have bit 2 set, so `power[12] = 2`. 
 The first element has bit 1 set, but the second does not, so `power[13] = 1`. 
 Both elements have bit 0 set, so `power[14] = 2`. 
 

 All higher bits are unset in the first element, so the remaining entries are 0.

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
class Solution(object):
    def largestPower(self, nums):
        blocks = [list(nums)]
        res = []
        for b in range(14, -1, -1):
            total = 0
            new_blocks = []
            i = 0
            while i < len(blocks):
                blk = blocks[i]
                on = [x for x in blk if (x >> b) & 1]
                if len(on) == len(blk):
                    total += len(blk)
                    new_blocks.append(blk)
                    i += 1
                else:
                    total += len(on)
                    off = [x for x in blk if not (x >> b) & 1]
                    if on:
                        new_blocks.append(on)
                    new_blocks.append(off)
                    new_blocks.extend(blocks[i + 1:])
                    break
            blocks = new_blocks
            res.append(total)
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
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [1718. Construct the Lexicographically Largest Valid Sequence](../../1501-2000/1819-construct-the-lexicographically-largest-valid-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-largest-power-array/)
