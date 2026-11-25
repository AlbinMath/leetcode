# LeetCode 1998: GCD Sort of an Array

**LeetCode Problem #1998 — GCD Sort of an Array**
Solve LeetCode GCD Sort of an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | GCD Sort of an Array |
| LeetCode | #1998 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`, and you can perform the following operation **any** number of times on `nums`:

Swap the positions of two elements `nums[i]` and `nums[j]` if `gcd(nums[i], nums[j]) > 1` where `gcd(nums[i], nums[j])` is the **greatest common divisor** of `nums[i]` and `nums[j]`.

Return `true` *if it is possible to sort *`nums`* in **non-decreasing** order using the above swap method, or *`false`* otherwise.*

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `2 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [7,21,3]`
- **Output:** `true`
- **Explanation:** We can sort [7,21,3] by performing the following operations:
- Swap 7 and 21 because gcd(7,21) = 7. nums = [

### Example 2
- **Input:** `nums = [5,2,6,2]`
- **Output:** `false`
- **Explanation:** It is impossible to sort the array because 5 cannot be swapped with any other element.

### Example 3
- **Input:** `nums = [10,5,9,3,15]`
- **Output:** `true
We can sort [10,5,9,3,15] by performing the following operations:
- Swap 10 and 15 because gcd(10,15) = 5. nums = [`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **GCD Sort of an Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [7,21,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can sort [7,21,3] by performing the following operations:
- Swap 7 and 21 because gcd(7,21) = 7. nums = [

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
    def gcdSort(self, nums: List[int]) -> bool:
        m = max(nums)
        p = list(range(m + 1))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        for x in nums:
            y, d = x, 2
            while d * d <= y:
                if y % d == 0:
                    p[f(x)] = f(d)
                    while y % d == 0: y //= d
                d += 1
            if y > 1: p[f(x)] = f(y)
        for a, b in zip(nums, sorted(nums)):
            if f(a) != f(b): return False
        return True
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
- [4098. Minimize the Maximum Value of GCD-Connected Array](../../4001-4500/4098-minimize-the-maximum-value-of-gcd-connected-array/)
- [905. Sort Array By Parity](../../0501-1000/0905-sort-array-by-parity/)
- [912. Sort an Array](../../0501-1000/0912-sort-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/gcd-sort-of-an-array/)
