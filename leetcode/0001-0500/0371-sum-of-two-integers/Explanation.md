# LeetCode 371: Sum of Two Integers

**LeetCode Problem #371 — Sum of Two Integers**
Solve LeetCode Sum of Two Integers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Two Integers |
| LeetCode | #371 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `a` and `b`, return *the sum of the two integers without using the operators* `+` *and* `-`.

## Constraints
- `-1000 <= a, b <= 1000`

## Examples
### Example 1
- **Input:** `a = 1, b = 2`
- **Output:** `3`

### Example 2
- **Input:** `a = 2, b = 3`
- **Output:** `5`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Two Integers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 1, b = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < 0x80000000 else ~(a ^ mask)
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
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1317-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [3890. Integers With Multiple Sum of Two Cubes](../../3501-4000/3890-integers-with-multiple-sum-of-two-cubes/)
- [29. Divide Two Integers](../../0001-0500/0029-divide-two-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-two-integers/)
