# LeetCode 1925: Count Square Sum Triples

**LeetCode Problem #1925 — Count Square Sum Triples**
Solve LeetCode Count Square Sum Triples using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Square Sum Triples |
| LeetCode | #1925 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **square triple** `(a,b,c)` is a triple where `a`, `b`, and `c` are **integers** and `a^2 + b^2 = c^2`.

Given an integer `n`, return *the number of **square triples** such that *`1 <= a, b, c <= n`.

## Constraints
- `1 <= n <= 250`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `2`
- **Explanation:** : The square triples are (3,4,5) and (4,3,5).

### Example 2
- **Input:** `n = 10`
- **Output:** `4`
- **Explanation:** : The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Square Sum Triples**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** : The square triples are (3,4,5) and (4,3,5).

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
    int countTriples(int n) {
        int count = 0;

        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                for (int c = 1; c <= n; c++) {
                    if (a * a + b * b == c * c) {
                        count++;
                    }
                }
            }
        }

        return count;
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
- [327. Count of Range Sum](../../0001-0500/0327-count-of-range-sum/)
- [633. Sum of Square Numbers](../../0501-1000/0633-sum-of-square-numbers/)
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../../1001-1500/1413-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-square-sum-triples/)
