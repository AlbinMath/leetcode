# LeetCode 600: Non-negative Integers without Consecutive Ones

**LeetCode Problem #600 — Non-negative Integers without Consecutive Ones**
Solve LeetCode Non-negative Integers without Consecutive Ones using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Non-negative Integers without Consecutive Ones |
| LeetCode | #600 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer `n`, return the number of the integers in the range `[0, n]` whose binary representations **do not** contain consecutive ones.

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `5`
- **Explanation:** Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.

### Example 2
- **Input:** `n = 1`
- **Output:** `2`

### Example 3
- **Input:** `n = 2`
- **Output:** `3`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Non-negative Integers without Consecutive Ones**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.

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
    def findIntegers(self, n: int) -> int:
        f = [0] * 32
        f[0], f[1] = 1, 2
        for i in range(2, 32):
            f[i] = f[i-1] + f[i-2]
        s = bin(n)[2:]
        ans, prev = 0, 0
        for i, b in enumerate(s):
            if b == '1':
                ans += f[len(s)-i-1]
                if prev:
                    return ans
                prev = 1
            else:
                prev = 0
        return ans + 1
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
- [3819. Rotate Non Negative Elements](../../4001-4500/4171-rotate-non-negative-elements/)
- [485. Max Consecutive Ones](../../0001-0500/0485-max-consecutive-ones/)
- [1004. Max Consecutive Ones III](../../1001-1500/1046-max-consecutive-ones-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/)
