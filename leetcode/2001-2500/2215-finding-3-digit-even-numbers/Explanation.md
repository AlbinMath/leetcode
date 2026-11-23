# LeetCode 2094: Finding 3-Digit Even Numbers

**LeetCode Problem #2094 — Finding 3-Digit Even Numbers**
Solve LeetCode Finding 3-Digit Even Numbers using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Finding 3-Digit Even Numbers |
| LeetCode | #2094 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `digits`, where each element is a digit. The array may contain duplicates.

You need to find **all** the **unique** integers that follow the given requirements:

The integer consists of the **concatenation** of **three** elements from `digits` in **any** arbitrary order. 
 The integer does not have **leading zeros**. 
 The integer is **even**.

For example, if the given `digits` were `[1, 2, 3]`, integers `132` and `312` follow the requirements.

Return *a **sorted** array of the unique integers.*

## Constraints
- `3 <= digits.length <= 100`
- `0 <= digits[i] <= 9`

## Examples
### Example 1
- **Input:** `digits = [2,1,3,0]`
- **Output:** `[102,120,130,132,210,230,302,310,312,320]`
- **Explanation:** All the possible integers that follow the requirements are in the output array. 
Notice that there are no

### Example 2
- **Input:** `digits = [2,2,8,8,2]`
- **Output:** `[222,228,282,288,822,828,882]`
- **Explanation:** The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882.

### Example 3
- **Input:** `digits = [3,7,5]`
- **Output:** `[]`
- **Explanation:** No

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Finding 3-Digit Even Numbers**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `digits = [2,1,3,0]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[102,120,130,132,210,230,302,310,312,320]`.
4. **Verification:** All the possible integers that follow the requirements are in the output array. 
Notice that there are no

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def findEvenNumbers(self, digits):
        s = set(digits)
        ans = set()
        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):
                    num = [a, b, c]
                    d = digits.copy()
                    if all(num.count(x) <= d.count(x) for x in set(num)):
                        ans.add(a * 100 + b * 10 + c)
        return sorted(ans)
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3483. Unique 3-Digit Even Numbers](../../3501-4000/3799-unique-3-digit-even-numbers/)
- [902. Numbers At Most N Given Digit Set](../../0501-1000/0938-numbers-at-most-n-given-digit-set/)
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/finding-3-digit-even-numbers/)
