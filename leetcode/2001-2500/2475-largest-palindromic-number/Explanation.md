# LeetCode 2384: Largest Palindromic Number

**LeetCode Problem #2384 — Largest Palindromic Number**
Solve LeetCode Largest Palindromic Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Palindromic Number |
| LeetCode | #2384 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `num` consisting of digits only.

Return *the **largest palindromic** integer (in the form of a string) that can be formed using digits taken from *`num`. It should not contain **leading zeroes**.

**Notes:**

You do **not** need to use all the digits of `num`, but you must use **at least** one digit. 
 The digits can be reordered.

## Constraints
- `1 <= num.length <= 10^5`
- `num` consists of digits.

## Examples
### Example 1
- **Input:** `num = "444947137"`
- **Output:** `"7449447"`
- **Explanation:** Use the digits "4449477" from "

### Example 2
- **Input:** `num = "00009"`
- **Output:** `"9"`
- **Explanation:** It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Palindromic Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "444947137"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"7449447"`.
4. **Verification:** Use the digits "4449477" from "

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
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10
        for ch in num:
            freq[int(ch)] += 1
            
        left_half = []
        
        for d in range(9, -1, -1):
            if d == 0 and not left_half:
                break
            pairs = freq[d] // 2
            if pairs > 0:
                left_half.append(str(d) * pairs)
                freq[d] %= 2
                
        mid = ""
        for d in range(9, -1, -1):
            if freq[d] > 0:
                mid = str(d)
                break
                
        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]
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
- [179. Largest Number](../../0001-0500/0179-largest-number/)
- [586. Customer Placing the Largest Number of Orders](../../0501-1000/0586-customer-placing-the-largest-number-of-orders/)
- [747. Largest Number At Least Twice of Others](../../0501-1000/0748-largest-number-at-least-twice-of-others/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-palindromic-number/)
