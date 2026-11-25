# LeetCode 1300: Sum of Mutated Array Closest to Target

**LeetCode Problem #1300 — Sum of Mutated Array Closest to Target**
Solve LeetCode Sum of Mutated Array Closest to Target using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Mutated Array Closest to Target |
| LeetCode | #1300 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr` and a target value `target`, return the integer `value` such that when we change all the integers larger than `value` in the given array to be equal to `value`, the sum of the array gets as close as possible (in absolute difference) to `target`.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from `arr`.

## Constraints
- `1 <= arr.length <= 10^4`
- `1 <= arr[i], target <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [4,9,3], target = 10`
- **Output:** `3`
- **Explanation:** When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

### Example 2
- **Input:** `arr = [2,3,5], target = 10`
- **Output:** `5`

### Example 3
- **Input:** `arr = [60864,25176,27249,21296,20204], target = 56803`
- **Output:** `11361`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Mutated Array Closest to Target**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [4,9,3], target = 10`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def calc(v: int) -> int:
            return sum(x if x < v else v for x in arr)

        lo, hi = 0, max(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if calc(mid) >= target:
                hi = mid
            else:
                lo = mid + 1

        # lo is the smallest value with calc(lo) >= target (or max(arr))
        if lo > 0 and abs(calc(lo - 1) - target) <= abs(calc(lo) - target):
            return lo - 1
        return lo
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii-input-array-is-sorted/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [494. Target Sum](../../0001-0500/0494-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/)
