# LeetCode 3954: Sum of Compatible Numbers in Range I

**LeetCode Problem #3954 — Sum of Compatible Numbers in Range I**
Solve LeetCode Sum of Compatible Numbers in Range I using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Compatible Numbers in Range I |
| LeetCode | #3954 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `n` and `k`.

A **positive** integer `x` is called **compatible** if it satisfies both of the following conditions:

`abs(n - x) <= k` 
 `(n & x) == 0`

Return the sum of all **compatible** integers `x`.

**Note**:

Here, `&` denotes the **bitwise AND** operator. 
 The **absolute** difference between integers `i` and `j` is defined as `abs(i - j)`.

## Constraints
- `1 <= n <= 100`
- `1 <= k <= 100`

## Examples
### Example 1
- **Input:** `n = 2, k = 3`
- **Output:** `10`
- **Explanation:** The compatible integers are: 

 
 `x = 1`, since `abs(2 - 1) = 1` and `2 & 1 = 0`. 
 `x = 4`, since `abs(2 - 4) = 2` and `2 & 4 = 0`. 
 `x = 5`, since `abs(2 - 5) = 3` and `2 & 5 = 0`. 
 

 Thus, the answer is `1 + 4 + 5 = 10`.

### Example 2
- **Input:** `n = 5, k = 1`
- **Output:** `0`
- **Explanation:** There are no compatible integers in the range `[4, 6]`. Thus, the answer is 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Compatible Numbers in Range I**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, k = 3`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The compatible integers are: 

 
 `x = 1`, since `abs(2 - 1) = 1` and `2 & 1 = 0`. 
 `x = 4`, since `abs(2 - 4) = 2` and `2 & 4 = 0`. 
 `x = 5`, since `abs(2 - 5) = 3` and `2 & 5 = 0`. 
 

 Thus, the answer is `1 + 4 + 5 = 10`.

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
class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        total = 0
        for x in range(max(1, n - k), n + k + 1):
            if n & x == 0:
                total += x
        return total
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
- [3855. Sum of K-Digit Numbers in a Range](../../3501-4000/3855-sum-of-k-digit-numbers-in-a-range/)
- [129. Sum Root to Leaf Numbers](../../0001-0500/0129-sum-root-to-leaf-numbers/)
- [303. Range Sum Query - Immutable](../../0001-0500/0303-range-sum-query-immutable/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/)
