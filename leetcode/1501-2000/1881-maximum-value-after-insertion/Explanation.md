# LeetCode 1881: Maximum Value after Insertion

**LeetCode Problem #1881 — Maximum Value after Insertion**
Solve LeetCode Maximum Value after Insertion using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value after Insertion |
| LeetCode | #1881 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a very large integer `n`, represented as a string,​​​​​​ and an integer digit `x`. The digits in `n` and the digit `x` are in the **inclusive** range `[1, 9]`, and `n` may represent a negative number.

You want to **maximize **`n`**'s numerical value** by inserting `x` anywhere in the decimal representation of `n`​​​​​​. You **cannot** insert `x` to the left of the negative sign.

For example, if `n = 73` and `x = 6`, it would be best to insert it between `7` and `3`, making `n = 763`. 
 If `n = -55` and `x = 2`, it would be best to insert it before the first `5`, making `n = -255`.

Return *a string representing the **maximum** value of *`n`*​​​​​​ after the insertion*.

## Constraints
- `1 <= n.length <= 10^5`
- `1 <= x <= 9`
- The digits in `n`​​​ are in the range `[1, 9]`.
- `n` is a valid representation of an integer.
- In the case of a negative `n`,​​​​​​ it will begin with `'-'`.

## Examples
### Example 1
- **Input:** `n = "99", x = 9`
- **Output:** `"999"`
- **Explanation:** The result is the same regardless of where you insert 9.

### Example 2
- **Input:** `n = "-13", x = 2`
- **Output:** `"-123"`
- **Explanation:** You can make n one of {-213, -123, -132}, and the largest of those three is -123.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Value after Insertion**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = "99", x = 9`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"999"`.
4. **Verification:** The result is the same regardless of where you insert 9.

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
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        d = str(x)
        start = 1 if n[0] == '-' else 0

        for i in range(start, len(n)):
            if start == 0 and n[i] < d:
                return n[:i] + d + n[i:]
            if start == 1 and n[i] > d:
                return n[:i] + d + n[i:]

        return n + d
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
- [4058. Maximum Pulse Value After One Subarray Rotation](../../4001-4500/4058-maximum-pulse-value-after-one-subarray-rotation/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)
- [1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](../../1001-1500/1465-maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-after-insertion/)
