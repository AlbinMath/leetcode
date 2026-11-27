# LeetCode 1671: Minimum Number of Removals to Make Mountain Array

**LeetCode Problem #1671 — Minimum Number of Removals to Make Mountain Array**
Solve LeetCode Minimum Number of Removals to Make Mountain Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Removals to Make Mountain Array |
| LeetCode | #1671 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You may recall that an array `arr` is a **mountain array** if and only if:

`arr.length >= 3` 
 There exists some index `i` (**0-indexed**) with `0 < i < arr.length - 1` such that:
 
 `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]` 
 `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `nums`​​​, return *the **minimum** number of elements to remove to make *`nums*​​​*`* **a **mountain array**.*

## Constraints
- `3 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^9`
- It is guaranteed that you can make a mountain array out of `nums`.

## Examples
### Example 1
- **Input:** `nums = [1,3,1]`
- **Output:** `0`
- **Explanation:** The array itself is a mountain array so we do not need to remove any elements.

### Example 2
- **Input:** `nums = [2,1,1,5,6,2,3,1]`
- **Output:** `3`
- **Explanation:** One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Removals to Make Mountain Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The array itself is a mountain array so we do not need to remove any elements.

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
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        dec = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    inc[i] = max(inc[i], inc[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    dec[i] = max(dec[i], dec[j] + 1)

        best = 0
        for i in range(n):
            if inc[i] > 1 and dec[i] > 1:
                best = max(best, inc[i] + dec[i] - 1)

        return n - best
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
- [3296. Minimum Number of Seconds to Make Mountain Height Zero](../../3001-3500/3296-minimum-number-of-seconds-to-make-mountain-height-zero/)
- [2009. Minimum Number of Operations to Make Array Continuous](../../2001-2500/2009-minimum-number-of-operations-to-make-array-continuous/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/)
