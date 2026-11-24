# LeetCode 1672: Richest Customer Wealth

**LeetCode Problem #1672 — Richest Customer Wealth**
Solve LeetCode Richest Customer Wealth using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Richest Customer Wealth |
| LeetCode | #1672 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i​​​​​^​​​​​​th​​​​` customer has in the `j​​​​​^​​​​​​th`​​​​ bank. Return* the **wealth** that the richest customer has.*

A customer's **wealth** is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum **wealth**.

## Constraints
- `m == accounts.length`
- `n == accounts[i].length`
- `1 <= m, n <= 50`
- `1 <= accounts[i][j] <= 100`

## Examples
### Example 1
- **Input:** `accounts = [[1,2,3],[3,2,1]]`
- **Output:** `6`

### Example 2
- **Input:** `accounts = [[1,5],[7,3],[3,5]]`
- **Output:** `10`
- **Explanation:** : 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

### Example 3
- **Input:** `accounts = [[2,8,7],[7,1,3],[1,9,5]]`
- **Output:** `17`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Richest Customer Wealth**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `accounts = [[1,2,3],[3,2,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.

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
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;

        for (int i = 0; i < accounts.size(); i++) {
            int wealth = 0;

            for (int j = 0; j < accounts[i].size(); j++) {
                wealth += accounts[i][j];
            }

            maxWealth = max(maxWealth, wealth);
        }

        return maxWealth;
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
- [2558. Take Gifts From the Richest Pile](../../2501-3000/2558-take-gifts-from-the-richest-pile/)
- [584. Find Customer Referee](../../0501-1000/0584-find-customer-referee/)
- [586. Customer Placing the Largest Number of Orders](../../0501-1000/0586-customer-placing-the-largest-number-of-orders/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/richest-customer-wealth/)
