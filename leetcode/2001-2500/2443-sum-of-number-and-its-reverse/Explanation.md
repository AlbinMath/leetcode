# LeetCode 2443: Sum of Number and Its Reverse

**LeetCode Problem #2443 — Sum of Number and Its Reverse**
Solve LeetCode Sum of Number and Its Reverse using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Number and Its Reverse |
| LeetCode | #2443 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **non-negative** integer `num`, return `true`* if *`num`* can be expressed as the sum of any **non-negative** integer and its reverse, or *`false`* otherwise.*

## Constraints
- `0 <= num <= 10^5`

## Examples
### Example 1
- **Input:** `num = 443`
- **Output:** `true`
- **Explanation:** 172 + 271 = 443, where 271 is the reverse of 172. Therefore, we return true.

### Example 2
- **Input:** `num = 63`
- **Output:** `false`
- **Explanation:** 63 cannot be expressed as the sum of a non-negative integer and its reverse. Therefore, we return false.

### Example 3
- **Input:** `num = 181`
- **Output:** `true`
- **Explanation:** 140 + 041 = 181, where 041 represents 41, the reverse of 140. Reversed numbers may contain leading zeros. Therefore, we return true.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Number and Its Reverse**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 443`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 172 + 271 = 443, where 271 is the reverse of 172. Therefore, we return true.

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
class Solution(object):
    def sumOfNumberAndReverse(self, num):
        return any(x + int(str(x)[::-1]) == num for x in range(num // 2, num + 1))
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
- [3918. Sum of Primes Between Number and Its Reverse](../../3501-4000/3918-sum-of-primes-between-number-and-its-reverse/)
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1001-1500/1498-number-of-subsequences-that-satisfy-the-given-sum-condition/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-number-and-its-reverse/)
