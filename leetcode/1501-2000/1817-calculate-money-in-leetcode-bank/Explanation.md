# LeetCode 1716: Calculate Money in Leetcode Bank

**LeetCode Problem #1716 — Calculate Money in Leetcode Bank**
Solve LeetCode Calculate Money in Leetcode Bank using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Calculate Money in Leetcode Bank |
| LeetCode | #1716 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Hercy wants to save money for his first car. He puts money in the Leetcode bank **every day**.

He starts by putting in `$1` on Monday, the first day. Every day from Tuesday to Sunday, he will put in `$1` more than the day before. On every subsequent Monday, he will put in `$1` more than the **previous Monday**.

Given `n`, return *the total amount of money he will have in the Leetcode bank at the end of the *`n^th`* day.*

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `10`
- **Explanation:** After the 4^th day, the total is 1 + 2 + 3 + 4 = 10.

### Example 2
- **Input:** `n = 10`
- **Output:** `37`
- **Explanation:** After the 10^th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2^nd Monday, Hercy only puts in $2.

### Example 3
- **Input:** `n = 20`
- **Output:** `96`
- **Explanation:** After the 20^th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Calculate Money in Leetcode Bank**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** After the 4^th day, the total is 1 + 2 + 3 + 4 = 10.

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
    int totalMoney(int n) {
        int money = 0;
        int monday = 1;

        for (int day = 0; day < n; day++) {
            money += monday + day % 7;
            
            if (day % 7 == 6) {
                monday++;
            }
        }

        return money;
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
- [1587. Bank Account Summary II](../../1501-2000/1734-bank-account-summary-ii/)
- [2043. Simple Bank System](../../2001-2500/2169-simple-bank-system/)
- [1873. Calculate Special Bonus](../../2001-2500/2024-calculate-special-bonus/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)
