# LeetCode 415: Add Strings

**LeetCode Problem #415 — Add Strings**
Solve LeetCode Add Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add Strings |
| LeetCode | #415 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two non-negative integers, `num1` and `num2` represented as string, return *the sum of* `num1` *and* `num2` *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`). You must also not convert the inputs to integers directly.

## Constraints
- `1 <= num1.length, num2.length <= 10^4`
- `num1` and `num2` consist of only digits.
- `num1` and `num2` don't have any leading zeros except for the zero itself.

## Examples
### Example 1
- **Input:** `num1 = "11", num2 = "123"`
- **Output:** `"134"`

### Example 2
- **Input:** `num1 = "456", num2 = "77"`
- **Output:** `"533"`

### Example 3
- **Input:** `num1 = "0", num2 = "0"`
- **Output:** `"0"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Add Strings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num1 = "11", num2 = "123"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"134"`.

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
    def addStrings(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = digit1 + digit2 + carry

            result.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return ''.join(reversed(result))
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
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [67. Add Binary](../../0001-0500/0067-add-binary/)
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-strings/)
