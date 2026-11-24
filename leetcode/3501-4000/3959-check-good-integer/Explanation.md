# LeetCode 3959: Check Good Integer

**LeetCode Problem #3959 — Check Good Integer**
Solve LeetCode Check Good Integer using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Good Integer |
| LeetCode | #3959 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n`.

Let `digitSum` be the sum of the digits of `n`, and let `squareSum` be the sum of the squares of the digits of `n`.

An integer is called **good** if `squareSum - digitSum >= 50`.

Return `true` if `n` is good. Otherwise, return `false`.

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 1000`
- **Output:** `false`
- **Explanation:** The digits of 1000 are 1, 0, 0, and 0. 
 The `digitSum` is `1 + 0 + 0 + 0 = 1`. 
 The `squareSum` is `1^2 + 0^2 + 0^2 + 0^2 = 1`. 
 The `squareSum - digitSum` is `1 - 1 = 0`. As 0 is not greater than or equal to 50, the output is `false`.

### Example 2
- **Input:** `n = 19`
- **Output:** `true`
- **Explanation:** The digits of 19 are 1 and 9. 
 The `digitSum` is `1 + 9 = 10`. 
 The `squareSum` is `1^2 + 9^2 = 1 + 81 = 82`. 
 The `squareSum - digitSum` is `82 - 10 = 72`. As 72 is greater than or equal to 50, the output is `true`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check Good Integer**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1000`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** The digits of 1000 are 1, 0, 0, and 0. 
 The `digitSum` is `1 + 0 + 0 + 0 = 1`. 
 The `squareSum` is `1^2 + 0^2 + 0^2 + 0^2 = 1`. 
 The `squareSum - digitSum` is `1 - 1 = 0`. As 0 is not greater than or equal to 50, the output is `false`.

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
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = square_sum = 0
        while n:
            d = n % 10
            digit_sum += d
            square_sum += d * d
            n //= 10
        return square_sum - digit_sum >= 50
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
- [1250. Check If It Is a Good Array](../../1001-1500/1250-check-if-it-is-a-good-array/)
- [2784. Check if Array is Good](../../2501-3000/2784-check-if-array-is-good/)
- [958. Check Completeness of a Binary Tree](../../0501-1000/0958-check-completeness-of-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-good-integer/)
