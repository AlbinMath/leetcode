# LeetCode 1017: Convert to Base -2

**LeetCode Problem #1017 — Convert to Base -2**
Solve LeetCode Convert to Base -2 using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert to Base -2 |
| LeetCode | #1017 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *a binary string representing its representation in base* `-2`.

**Note** that the returned string should not have leading zeros unless the string is `"0"`.

## Constraints
- `0 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `"110"`

### Example 2
- **Input:** `n = 3`
- **Output:** `"111"`

### Example 3
- **Input:** `n = 4`
- **Output:** `"100"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Convert to Base -2**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"110"`.

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
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
            
        bits = []
        while n != 0:
            bits.append(str(n & 1))
            n = -(n >> 1)
            
        return "".join(reversed(bits))
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
- [108. Convert Sorted Array to Binary Search Tree](../../0001-0500/0108-convert-sorted-array-to-binary-search-tree/)
- [109. Convert Sorted List to Binary Search Tree](../../0001-0500/0109-convert-sorted-list-to-binary-search-tree/)
- [405. Convert a Number to Hexadecimal](../../0001-0500/0405-convert-a-number-to-hexadecimal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-to-base-2/)
