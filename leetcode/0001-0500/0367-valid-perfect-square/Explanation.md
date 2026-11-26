# LeetCode 367: Valid Perfect Square

**LeetCode Problem #367 — Valid Perfect Square**
Solve LeetCode Valid Perfect Square using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Perfect Square |
| LeetCode | #367 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer num, return `true` *if* `num` *is a perfect square or* `false` *otherwise*.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

## Constraints
- `1 <= num <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `num = 16`
- **Output:** `true`
- **Explanation:** We return true because 4 * 4 = 16 and 4 is an integer.

### Example 2
- **Input:** `num = 14`
- **Output:** `false`
- **Explanation:** We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Valid Perfect Square**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 16`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We return true because 4 * 4 = 16 and 4 is an integer.

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
    def isPerfectSquare(self, num):
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True

            elif square < num:
                left = mid + 1

            else:
                right = mid - 1

        return False
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
- [3715. Sum of Perfect Square Ancestors](../../3501-4000/3715-sum-of-perfect-square-ancestors/)
- [279. Perfect Squares](../../0001-0500/0279-perfect-squares/)
- [391. Perfect Rectangle](../../0001-0500/0391-perfect-rectangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-perfect-square/)
