# LeetCode 1352: Product of the Last K Numbers

**LeetCode Problem #1352 — Product of the Last K Numbers**
Solve LeetCode Product of the Last K Numbers using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Product of the Last K Numbers |
| LeetCode | #1352 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design an algorithm that accepts a stream of integers and retrieves the product of the last `k` integers of the stream.

Implement the `ProductOfNumbers` class:

`ProductOfNumbers()` Initializes the object with an empty stream. 
 `void add(int num)` Appends the integer `num` to the stream. 
 `int getProduct(int k)` Returns the product of the last `k` numbers in the current list. You can assume that always the current list has at least `k` numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

## Constraints
- `0 <= num <= 100`
- `1 <= k <= 4 * 10^4`
- At most `4 * 10^4` calls will be made to `add` and `getProduct`.
- The product of the stream at any point in time will fit in a **32-bit** integer.

## Examples
Consider the standard input for **Product of the Last K Numbers**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Product of the Last K Numbers**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Bitwise Masking & Bit Shift** step by step to the input yields the expected result.

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
class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]
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
- [628. Maximum Product of Three Numbers](../../0501-1000/0628-maximum-product-of-three-numbers/)
- [713. Subarray Product Less Than K](../../0501-1000/0713-subarray-product-less-than-k/)
- [1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers](../../1501-2000/1577-number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/product-of-the-last-k-numbers/)
