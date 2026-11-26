# LeetCode 402: Remove K Digits

**LeetCode Problem #402 — Remove K Digits**
Solve LeetCode Remove K Digits using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove K Digits |
| LeetCode | #402 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given string num representing a non-negative integer `num`, and an integer `k`, return *the smallest possible integer after removing* `k` *digits from* `num`.

## Constraints
- `1 <= k <= num.length <= 10^5`
- `num` consists of only digits.
- `num` does not have any leading zeros except for the zero itself.

## Examples
### Example 1
- **Input:** `num = "1432219", k = 3`
- **Output:** `"1219"`
- **Explanation:** Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

### Example 2
- **Input:** `num = "10200", k = 1`
- **Output:** `"200"`
- **Explanation:** Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

### Example 3
- **Input:** `num = "10", k = 2`
- **Output:** `"0"`
- **Explanation:** Remove all the digits from the number and it is left with nothing which is 0.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove K Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "1432219", k = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"1219"`.
4. **Verification:** Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)

        if k:
            stack = stack[:-k]

        res = ''.join(stack).lstrip('0')
        return res or '0'
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3703. Remove K-Balanced Substrings](../../3501-4000/3703-remove-k-balanced-substrings/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [1837. Sum of Digits in Base K](../../1501-2000/1837-sum-of-digits-in-base-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-k-digits/)
