# LeetCode 2310: Sum of Numbers With Units Digit K

**LeetCode Problem #2310 — Sum of Numbers With Units Digit K**
Solve LeetCode Sum of Numbers With Units Digit K using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Numbers With Units Digit K |
| LeetCode | #2310 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `num` and `k`, consider a set of positive integers with the following properties:

The units digit of each integer is `k`. 
 The sum of the integers is `num`.

Return *the **minimum** possible size of such a set, or *`-1`* if no such set exists.*

The set can contain multiple instances of the same integer, and the sum of an empty set is considered `0`. 
 The **units digit** of a number is the rightmost digit of the number.

## Constraints
- `0 <= num <= 3000`
- `0 <= k <= 9`

## Examples
### Example 1
- **Input:** `num = 58, k = 9`
- **Output:** `2`
- **Explanation:** One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
Another valid set is [19,39].
It can be shown that 2 is the minimum possible size of a valid set.

### Example 2
- **Input:** `num = 37, k = 2`
- **Output:** `-1`
- **Explanation:** It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.

### Example 3
- **Input:** `num = 0, k = 7`
- **Output:** `0`
- **Explanation:** The sum of an empty set is considered 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Numbers With Units Digit K**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 58, k = 9`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
Another valid set is [19,39].
It can be shown that 2 is the minimum possible size of a valid set.

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
    def minimumNumbers(self, num, k):
        if num == 0:
            return 0
            
        for m in range(1, 11):
            if m * k <= num and (m * k) % 10 == num % 10:
                return m
                
        return -1
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
- [3855. Sum of K-Digit Numbers in a Range](../../3501-4000/3855-sum-of-k-digit-numbers-in-a-range/)
- [2081. Sum of k-Mirror Numbers](../../2001-2500/2081-sum-of-k-mirror-numbers/)
- [902. Numbers At Most N Given Digit Set](../../0501-1000/0902-numbers-at-most-n-given-digit-set/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/)
