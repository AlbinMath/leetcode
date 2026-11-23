# LeetCode 509: Fibonacci Number

**LeetCode Problem #509 — Fibonacci Number**
Solve LeetCode Fibonacci Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fibonacci Number |
| LeetCode | #509 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The Fibonacci numbers , commonly denoted `F(n)` form a sequence, called the Fibonacci sequence , such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given `n`, calculate `F(n)`.

## Constraints
- `0 <= n <= 30`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `1`
- **Explanation:** F(2) = F(1) + F(0) = 1 + 0 = 1.

### Example 2
- **Input:** `n = 3`
- **Output:** `2`
- **Explanation:** F(3) = F(2) + F(1) = 1 + 1 = 2.

### Example 3
- **Input:** `n = 4`
- **Output:** `3`
- **Explanation:** F(4) = F(3) + F(2) = 2 + 1 = 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Fibonacci Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** F(2) = F(1) + F(0) = 1 + 0 = 1.

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
    def fib(self, n):
        prev = 0
        curr = 1

        for i in range(n):
            prev, curr = curr, prev + curr

        return prev
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
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0872-split-array-into-fibonacci-sequence/)
- [2648. Generate Fibonacci Sequence](../../2501-3000/2775-generate-fibonacci-sequence/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fibonacci-number/)
