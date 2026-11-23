# LeetCode 326: Power of Three

**LeetCode Problem #326 — Power of Three**
Solve LeetCode Power of Three using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Power of Three |
| LeetCode | #326 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3^x`.

## Constraints
- `-2^31 <= n <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `n = 27`
- **Output:** `true`
- **Explanation:** 27 = 3^3

### Example 2
- **Input:** `n = 0`
- **Output:** `false`
- **Explanation:** There is no x where 3^x = 0.

### Example 3
- **Input:** `n = -1`
- **Output:** `false`
- **Explanation:** There is no x where 3^x = (-1).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Power of Three**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 27`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 27 = 3^3

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
};
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
- [185. Department Top Three Salaries](../../0001-0500/0185-department-top-three-salaries/)
- [628. Maximum Product of Three Numbers](../../0501-1000/0628-maximum-product-of-three-numbers/)
- [1050. Actors and Directors Who Cooperated At Least Three Times](../../1001-1500/1136-actors-and-directors-who-cooperated-at-least-three-times/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/power-of-three/)
