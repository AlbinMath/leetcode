# LeetCode 1780: Check if Number is a Sum of Powers of Three

**LeetCode Problem #1780 — Check if Number is a Sum of Powers of Three**
Solve LeetCode Check if Number is a Sum of Powers of Three using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Number is a Sum of Powers of Three |
| LeetCode | #1780 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return `true` *if it is possible to represent *`n`* as the sum of distinct powers of three.* Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3^x`.

## Constraints
- `1 <= n <= 10^7`

## Examples
### Example 1
- **Input:** `n = 12`
- **Output:** `true`
- **Explanation:** 12 = 3^1 + 3^2

### Example 2
- **Input:** `n = 91`
- **Output:** `true`
- **Explanation:** 91 = 3^0 + 3^2 + 3^4

### Example 3
- **Input:** `n = 21`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Number is a Sum of Powers of Three**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 12`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 12 = 3^1 + 3^2

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
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
            
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
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2177-find-three-consecutive-integers-that-sum-to-a-given-number/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)
- [2283. Check if Number Has Equal Digit Count and Digit Value](../../2001-2500/2283-check-if-number-has-equal-digit-count-and-digit-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)
