# LeetCode 2259: Remove Digit From Number to Maximize Result

**LeetCode Problem #2259 — Remove Digit From Number to Maximize Result**
Solve LeetCode Remove Digit From Number to Maximize Result using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Digit From Number to Maximize Result |
| LeetCode | #2259 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `number` representing a **positive integer** and a character `digit`.

Return *the resulting string after removing **exactly one occurrence** of *`digit`* from *`number`* such that the value of the resulting string in **decimal** form is **maximized***. The test cases are generated such that `digit` occurs at least once in `number`.

## Constraints
- `2 <= number.length <= 100`
- `number` consists of digits from `'1'` to `'9'`.
- `digit` is a digit from `'1'` to `'9'`.
- `digit` occurs at least once in `number`.

## Examples
### Example 1
- **Input:** `number = "123", digit = "3"`
- **Output:** `"12"`
- **Explanation:** There is only one '3' in "123". After removing '3', the result is "12".

### Example 2
- **Input:** `number = "1231", digit = "1"`
- **Output:** `"231"`
- **Explanation:** We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".

### Example 3
- **Input:** `number = "551", digit = "5"`
- **Output:** `"51"`
- **Explanation:** We can remove either the first or second '5' from "551".
Both result in the string "51".

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Digit From Number to Maximize Result**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `number = "123", digit = "3"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"12"`.
4. **Verification:** There is only one '3' in "123". After removing '3', the result is "12".

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
class Solution(object):
    def removeDigit(self, number, digit):
        last_idx = -1
        for i, ch in enumerate(number):
            if ch == digit:
                last_idx = i
                if i + 1 < len(number) and number[i + 1] > digit:
                    return number[:i] + number[i + 1:]
        return number[:last_idx] + number[last_idx + 1:]
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
- [2605. Form Smallest Number From Two Digit Arrays](../../2501-3000/2605-form-smallest-number-from-two-digit-arrays/)
- [1771. Maximize Palindrome Length From Subsequences](../../1501-2000/1771-maximize-palindrome-length-from-subsequences/)
- [1808. Maximize Number of Nice Divisors](../../1501-2000/1808-maximize-number-of-nice-divisors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/)
