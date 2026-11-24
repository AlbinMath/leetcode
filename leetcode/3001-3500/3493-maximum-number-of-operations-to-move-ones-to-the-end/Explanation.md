# LeetCode 3228: Maximum Number of Operations to Move Ones to the End

**LeetCode Problem #3228 — Maximum Number of Operations to Move Ones to the End**
Solve LeetCode Maximum Number of Operations to Move Ones to the End using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Operations to Move Ones to the End |
| LeetCode | #3228 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s`.

You can perform the following operation on the string **any** number of times:

Choose **any** index `i` from the string where `i + 1 < s.length` such that `s[i] == '1'` and `s[i + 1] == '0'`. 
 Move the character `s[i]` to the **right** until it reaches the end of the string or another `'1'`. For example, for `s = "010010"`, if we choose `i = 1`, the resulting string will be `s = "0** 001 **10"`.

Return the **maximum** number of operations that you can perform.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "1001101"`
- **Output:** `4`
- **Explanation:** We can perform the following operations: 

 
 Choose index `i = 0`. The resulting string is s = "

### Example 2
- **Input:** `s = "00111"`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Operations to Move Ones to the End**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1001101"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can perform the following operations: 

 
 Choose index `i = 0`. The resulting string is s = "

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
    def maxOperations(self, s: str) -> int:
        ones = 0
        ops = 0
        
        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            elif i > 0 and s[i - 1] == '1':
                ops += ones
                
        return ops
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
- [3038. Maximum Number of Operations With the Same Score I](../../3001-3500/3320-maximum-number-of-operations-with-the-same-score-i/)
- [3040. Maximum Number of Operations With the Same Score II](../../3001-3500/3318-maximum-number-of-operations-with-the-same-score-ii/)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1895-minimum-number-of-operations-to-move-all-balls-to-each-box/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/)
