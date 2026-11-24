# LeetCode 1952: Three Divisors

**LeetCode Problem #1952 — Three Divisors**
Solve LeetCode Three Divisors using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Three Divisors |
| LeetCode | #1952 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return `true`* if *`n`* has **exactly three positive divisors**. Otherwise, return *`false`.

An integer `m` is a **divisor** of `n` if there exists an integer `k` such that `n = k * m`.

## Constraints
- `1 <= n <= 10^4`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `false`

### Example 2
- **Input:** `n = 4`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Three Divisors**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.

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
    bool isThree(int n) {
        int root = sqrt(n);

        // n must be a perfect square
        if (root * root != n) {
            return false;
        }

        // Check whether the square root is prime
        if (root < 2) {
            return false;
        }

        for (int i = 2; i * i <= root; i++) {
            if (root % i == 0) {
                return false;
            }
        }

        return true;
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
- [1362. Closest Divisors](../../1001-1500/1362-closest-divisors/)
- [1390. Four Divisors](../../1001-1500/1390-four-divisors/)
- [1808. Maximize Number of Nice Divisors](../../1501-2000/1808-maximize-number-of-nice-divisors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/three-divisors/)
