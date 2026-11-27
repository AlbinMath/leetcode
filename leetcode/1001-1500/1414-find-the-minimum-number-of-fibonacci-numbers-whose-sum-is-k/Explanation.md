# LeetCode 1414: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

**LeetCode Problem #1414 — Find the Minimum Number of Fibonacci Numbers Whose Sum Is K**
Solve LeetCode Find the Minimum Number of Fibonacci Numbers Whose Sum Is K using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Minimum Number of Fibonacci Numbers Whose Sum Is K |
| LeetCode | #1414 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `k`, *return the minimum number of Fibonacci numbers whose sum is equal to *`k`. The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:

`F_1 = 1` 
 `F_2 = 1` 
 `F_n = F_n-1 + F_n-2` for `n > 2.` 
 
It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to `k`.

## Constraints
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `k = 7`
- **Output:** `2`
- **Explanation:** The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.

### Example 2
- **Input:** `k = 10`
- **Output:** `2`
- **Explanation:** For k = 10 we can use 2 + 8 = 10.

### Example 3
- **Input:** `k = 19`
- **Output:** `3`
- **Explanation:** For k = 19 we can use 1 + 5 + 13 = 19.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Minimum Number of Fibonacci Numbers Whose Sum Is K**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 7`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.

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
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] <= k:
            fib.append(fib[-1] + fib[-2])
        count = 0
        for f in reversed(fib):
            if k == 0:
                break
            if f <= k:
                k -= f
                count += 1
        return count
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
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [1679. Max Number of K-Sum Pairs](../../1501-2000/1679-max-number-of-k-sum-pairs/)
- [2081. Sum of k-Mirror Numbers](../../2001-2500/2081-sum-of-k-mirror-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)
