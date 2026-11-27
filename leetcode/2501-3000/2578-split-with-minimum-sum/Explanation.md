# LeetCode 2578: Split With Minimum Sum

**LeetCode Problem #2578 — Split With Minimum Sum**
Solve LeetCode Split With Minimum Sum using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split With Minimum Sum |
| LeetCode | #2578 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer `num`, split it into two non-negative integers `num1` and `num2` such that:

The concatenation of `num1` and `num2` is a permutation of `num`.

In other words, the sum of the number of occurrences of each digit in `num1` and `num2` is equal to the number of occurrences of that digit in `num`. 
 
 
 `num1` and `num2` can contain leading zeros.

Return *the **minimum** possible sum of* `num1` *and* `num2`.

**Notes:**

It is guaranteed that `num` does not contain any leading zeros. 
 The order of occurrence of the digits in `num1` and `num2` may differ from the order of occurrence of `num`.

## Constraints
- `10 <= num <= 10^9`

## Examples
### Example 1
- **Input:** `num = 4325`
- **Output:** `59`
- **Explanation:** We can split 4325 so that `num1` is 24 and `num2` is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.

### Example 2
- **Input:** `num = 687`
- **Output:** `75`
- **Explanation:** We can split 687 so that `num1` is 68 and `num2` is 7, which would give an optimal sum of 75.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Split With Minimum Sum**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 4325`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `59`.
4. **Verification:** We can split 4325 so that `num1` is 24 and `num2` is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.

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
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        a = ''.join(digits[0::2])
        b = ''.join(digits[1::2])
        return int(a) + int(b or '0')
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
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [2547. Minimum Cost to Split an Array](../../2501-3000/2547-minimum-cost-to-split-an-array/)
- [3698. Split Array With Minimum Difference](../../3501-4000/3698-split-array-with-minimum-difference/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-with-minimum-sum/)
