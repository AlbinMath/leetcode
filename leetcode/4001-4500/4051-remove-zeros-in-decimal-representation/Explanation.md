# LeetCode 3726: Remove Zeros in Decimal Representation

**LeetCode Problem #3726 — Remove Zeros in Decimal Representation**
Solve LeetCode Remove Zeros in Decimal Representation using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Zeros in Decimal Representation |
| LeetCode | #3726 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **positive** integer `n`.

Return the integer obtained by removing all zeros from the decimal representation of `n`.

## Constraints
- `1 <= n <= 10^15`

## Examples
### Example 1
- **Input:** `n = 1020030`
- **Output:** `123`
- **Explanation:** After removing all zeros from 1

### Example 2
- **Input:** `n = 1`
- **Output:** `1`
- **Explanation:** 1 has no zero in its decimal representation. Therefore, the answer is 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Zeros in Decimal Representation**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1020030`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `123`.
4. **Verification:** After removing all zeros from 1

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
    def removeZeros(self, n: int) -> int:
        res, mul = 0, 1
        while n:
            d = n % 10
            if d:
                res += d * mul
                mul *= 10
            n //= 10
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
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0767-prime-number-of-set-bits-in-binary-representation/)
- [1238. Circular Permutation in Binary Representation](../../1001-1500/1359-circular-permutation-in-binary-representation/)
- [1404. Number of Steps to Reduce a Number in Binary Representation to One](../../1501-2000/1520-number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-zeros-in-decimal-representation/)
