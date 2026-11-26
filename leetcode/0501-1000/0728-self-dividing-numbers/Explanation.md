# LeetCode 728: Self Dividing Numbers

**LeetCode Problem #728 — Self Dividing Numbers**
Solve LeetCode Self Dividing Numbers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Self Dividing Numbers |
| LeetCode | #728 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **self-dividing number** is a number that is divisible by every digit it contains.

For example, `128` is **a self-dividing number** because `128 % 1 == 0`, `128 % 2 == 0`, and `128 % 8 == 0`.

A **self-dividing number** is not allowed to contain the digit zero.

Given two integers `left` and `right`, return *a list of all the **self-dividing numbers** in the range* `[left, right]` (both **inclusive**).

## Constraints
- `1 <= left <= right <= 10^4`

## Examples
### Example 1
- **Input:** `left = 1, right = 22`
- **Output:** `[1,2,3,4,5,6,7,8,9,11,12,15,22]`

### Example 2
- **Input:** `left = 47, right = 85`
- **Output:** `[48,55,66,77]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Self Dividing Numbers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `left = 1, right = 22`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4,5,6,7,8,9,11,12,15,22]`.

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
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res = []
        for n in range(left, right + 1):
            s = str(n)
            if '0' not in s and all(n % int(d) == 0 for d in s):
                res.append(n)
        return res
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
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [238. Product of Array Except Self](../../0001-0500/0238-product-of-array-except-self/)
- [335. Self Crossing](../../0001-0500/0335-self-crossing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/self-dividing-numbers/)
