# LeetCode 1304: Find N Unique Integers Sum up to Zero

**LeetCode Problem #1304 — Find N Unique Integers Sum up to Zero**
Solve LeetCode Find N Unique Integers Sum up to Zero using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find N Unique Integers Sum up to Zero |
| LeetCode | #1304 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return **any** array containing `n` **unique** integers such that they add up to `0`.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `[-7,-1,1,3,4]`
- **Explanation:** These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

### Example 2
- **Input:** `n = 3`
- **Output:** `[-1,0,1]`

### Example 3
- **Input:** `n = 1`
- **Output:** `[0]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find N Unique Integers Sum up to Zero**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[-7,-1,1,3,4]`.
4. **Verification:** These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

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
    def sumZero(self, n: int) -> list[int]:
        res = []
        if n % 2 == 1:
            res.append(0)
            
        for x in range(1, n // 2 + 1):
            res.append(x)
            res.append(-x)
            
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
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2177-find-three-consecutive-integers-that-sum-to-a-given-number/)
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1317-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](../../1001-1500/1414-find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)
