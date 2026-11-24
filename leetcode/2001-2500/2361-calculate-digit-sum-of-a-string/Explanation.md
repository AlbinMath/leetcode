# LeetCode 2243: Calculate Digit Sum of a String

**LeetCode Problem #2243 — Calculate Digit Sum of a String**
Solve LeetCode Calculate Digit Sum of a String using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Calculate Digit Sum of a String |
| LeetCode | #2243 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of digits and an integer `k`.

A **round** can be completed if the length of `s` is greater than `k`. In one round, do the following:

**Divide** `s` into **consecutive groups** of size `k` such that the first `k` characters are in the first group, the next `k` characters are in the second group, and so on. **Note** that the size of the last group can be smaller than `k`. 
 **Replace** each group of `s` with a string representing the sum of all its digits. For example, `"346"` is replaced with `"13"` because `3 + 4 + 6 = 13`. 
 **Merge** consecutive groups together to form a new string. If the length of the string is greater than `k`, repeat from step `1`.

Return `s` *after all rounds have been completed*.

## Constraints
- `1 <= s.length <= 100`
- `2 <= k <= 100`
- `s` consists of digits only.

## Examples
### Example 1
- **Input:** `s = "11111222223", k = 3`
- **Output:** `"135"`
- **Explanation:** - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
 ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
 So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
- For the second round, we divide s into "346" and "5".
 Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
 So, s becomes "13" + "5" = "135" after second round. 
Now, s.length <= k, so we return "135" as the answer.

### Example 2
- **Input:** `s = "00000000", k = 3`
- **Output:** `"000"`
- **Explanation:** We divide s into "000", "000", and "00".
Then we calculate the digit sum of each group: 0 + 0 + 0 = 0, 0 + 0 + 0 = 0, and 0 + 0 = 0. 
s becomes "0" + "0" + "0" = "000", whose length is equal to k, so we return "000".

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Calculate Digit Sum of a String**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "11111222223", k = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"135"`.
4. **Verification:** - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
 ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
 So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
- For the second round, we divide s into "346" and "5".
 Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
 So, s becomes "13" + "5" = "135" after second round. 
Now, s.length <= k, so we return "135" as the answer.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                parts.append(str(sum(int(c) for c in chunk)))
            s = "".join(parts)
        return s
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1796. Second Largest Digit in a String](../../1501-2000/1904-second-largest-digit-in-a-string/)
- [1945. Sum of Digits of String After Convert](../../2001-2500/2076-sum-of-digits-of-string-after-convert/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculate-digit-sum-of-a-string/)
