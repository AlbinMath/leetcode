# LeetCode 3174: Clear Digits

**LeetCode Problem #3174 — Clear Digits**
Solve LeetCode Clear Digits using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Clear Digits |
| LeetCode | #3174 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`.

Your task is to remove **all** digits by doing this operation repeatedly:

Delete the *first* digit and the **closest** non-digit character to its *left*.

Return the resulting string after removing all digits.

**Note** that the operation *cannot* be performed on a digit that does not have any non-digit character to its left.

## Constraints
- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters and digits.
- The input is generated such that it is possible to delete all digits.

## Examples
### Example 1
- **Input:** `s = "abc"`
- **Output:** `"abc"`
- **Explanation:** There is no digit in the string.

### Example 2
- **Input:** `s = "cb34"`
- **Output:** `""`
- **Explanation:** First, we apply the operation on `s[2]`, and `s` becomes `"c4"`. 

 Then we apply the operation on `s[1]`, and `s` becomes `""`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Clear Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abc"`.
4. **Verification:** There is no digit in the string.

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
    def clearDigits(self, s: str) -> str:
        stk = []
        
        for c in s:
            if c.isdigit():
                if stk:
                    stk.pop()
            else:
                stk.append(c)
                
        return "".join(stk)
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
- [258. Add Digits](../../0001-0500/0258-add-digits/)
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)
- [402. Remove K Digits](../../0001-0500/0402-remove-k-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/clear-digits/)
