# LeetCode 537: Complex Number Multiplication

**LeetCode Problem #537 — Complex Number Multiplication**
Solve LeetCode Complex Number Multiplication using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Complex Number Multiplication |
| LeetCode | #537 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A complex number can be represented as a string on the form `"**real**+**imaginary**i"` where:

`real` is the real part and is an integer in the range `[-100, 100]`. 
 `imaginary` is the imaginary part and is an integer in the range `[-100, 100]`. 
 `i^2 == -1`.

Given two complex numbers `num1` and `num2` as strings, return *a string of the complex number that represents their multiplications*.

## Constraints
- `num1` and `num2` are valid complex numbers.

## Examples
### Example 1
- **Input:** `num1 = "1+1i", num2 = "1+1i"`
- **Output:** `"0+2i"`
- **Explanation:** (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

### Example 2
- **Input:** `num1 = "1+-1i", num2 = "1+-1i"`
- **Output:** `"0+-2i"`
- **Explanation:** (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Complex Number Multiplication**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num1 = "1+1i", num2 = "1+1i"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"0+2i"`.
4. **Verification:** (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

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
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num: str):
            real, imag = num.split('+')
            return int(real), int(imag[:-1])

        a, b = parse(num1)
        c, d = parse(num2)

        real = a * c - b * d
        imag = a * d + b * c
        return f"{real}+{imag}i"
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
- [668. Kth Smallest Number in Multiplication Table](../../0501-1000/0668-kth-smallest-number-in-multiplication-table/)
- [3264. Final Array State After K Multiplication Operations I](../../3001-3500/3264-final-array-state-after-k-multiplication-operations-i/)
- [3266. Final Array State After K Multiplication Operations II](../../3001-3500/3266-final-array-state-after-k-multiplication-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/complex-number-multiplication/)
