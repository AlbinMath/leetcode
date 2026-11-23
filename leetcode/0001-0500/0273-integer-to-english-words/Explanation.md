# LeetCode 273: Integer to English Words

**LeetCode Problem #273 — Integer to English Words**
Solve LeetCode Integer to English Words using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Integer to English Words |
| LeetCode | #273 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Convert a non-negative integer `num` to its English words representation.

## Constraints
- `0 <= num <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `num = 123`
- **Output:** `"One Hundred Twenty Three"`

### Example 2
- **Input:** `num = 12345`
- **Output:** `"Twelve Thousand Three Hundred Forty Five"`

### Example 3
- **Input:** `num = 1234567`
- **Output:** `"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Integer to English Words**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 123`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"One Hundred Twenty Three"`.

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
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                   "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                   "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
                "Eighty", "Ninety"]
        scales = ["", "Thousand", "Million", "Billion"]

        def three(n):
            parts = []
            if n >= 100:
                parts.append(below20[n // 100])
                parts.append("Hundred")
                n %= 100
            if n >= 20:
                parts.append(tens[n // 10])
                n %= 10
            if n > 0:
                parts.append(below20[n])
            return parts

        words = []
        i = 0
        while num > 0:
            chunk = num % 1000
            if chunk:
                words = three(chunk) + ([scales[i]] if scales[i] else []) + words
            num //= 1000
            i += 1
        return " ".join(words)
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
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [12. Integer to Roman](../../0001-0500/0012-integer-to-roman/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/integer-to-english-words/)
