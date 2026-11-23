# LeetCode 397: Integer Replacement

**LeetCode Problem #397 — Integer Replacement**
Solve LeetCode Integer Replacement using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Integer Replacement |
| LeetCode | #397 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer `n`, you can apply one of the following operations:

If `n` is even, replace `n` with `n / 2`. 
 If `n` is odd, replace `n` with either `n + 1` or `n - 1`.

Return *the minimum number of operations needed for* `n` *to become* `1`.

## Constraints
- `1 <= n <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `n = 8`
- **Output:** `3`
- **Explanation:** 8 -> 4 -> 2 -> 1

### Example 2
- **Input:** `n = 7`
- **Output:** `4`
- **Explanation:** 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

### Example 3
- **Input:** `n = 4`
- **Output:** `2`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Integer Replacement**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 8`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** 8 -> 4 -> 2 -> 1

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
    def integerReplacement(self, n: int) -> int:
        steps = 0
        
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or (n & 3) == 1:
                # n ends in ...01 or is the special case 3
                n -= 1
            else:
                # n ends in ...11 and n > 3
                n += 1
            steps += 1
            
        return steps
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
- [424. Longest Repeating Character Replacement](../../0001-0500/0424-longest-repeating-character-replacement/)
- [3300. Minimum Element After Replacement With Digit Sum](../../3501-4000/3606-minimum-element-after-replacement-with-digit-sum/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/integer-replacement/)
