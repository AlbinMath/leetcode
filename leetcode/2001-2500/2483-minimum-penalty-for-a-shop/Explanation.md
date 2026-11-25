# LeetCode 2483: Minimum Penalty for a Shop

**LeetCode Problem #2483 — Minimum Penalty for a Shop**
Solve LeetCode Minimum Penalty for a Shop using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Penalty for a Shop |
| LeetCode | #2483 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the customer visit log of a shop represented by a **0-indexed** string `customers` consisting only of characters `'N'` and `'Y'`:

if the `i^th` character is `'Y'`, it means that customers come at the `i^th` hour 
 whereas `'N'` indicates that no customers come at the `i^th` hour.

If the shop closes at the `j^th` hour (`0 <= j <= n`), the **penalty** is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by `1`. 
 For every hour when the shop is closed and customers come, the penalty increases by `1`.

Return* the **earliest** hour at which the shop must be closed to incur a **minimum** penalty.*

**Note** that if a shop closes at the `j^th` hour, it means the shop is closed at the hour `j`.

## Constraints
- `1 <= customers.length <= 10^5`
- `customers` consists only of characters `'Y'` and `'N'`.

## Examples
### Example 1
- **Input:** `customers = "YYNY"`
- **Output:** `2`
- **Explanation:** - Closing the shop at the 0^th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1^st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2^nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3^rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4^th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2^nd or 4^th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

### Example 2
- **Input:** `customers = "NNNNN"`
- **Output:** `0`
- **Explanation:** It is best to close the shop at the 0^th hour as no customers arrive.

### Example 3
- **Input:** `customers = "YYYY"`
- **Output:** `4`
- **Explanation:** It is best to close the shop at the 4^th hour as customers arrive at each hour.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Penalty for a Shop**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `customers = "YYNY"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** - Closing the shop at the 0^th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1^st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2^nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3^rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4^th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2^nd or 4^th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var bestClosingTime = function(customers) {
    let penalty = 0;
    for (let char of customers) {
        if (char === 'Y') {
            penalty++;
        }
    }

    let minPenalty = penalty;
    let bestHour = 0;
    for (let i = 0; i < customers.length; i++) {
        if (customers[i] === 'Y') {
            penalty--;
        } else {
            penalty++;
        }
        if (penalty < minPenalty) {
            minPenalty = penalty;
            bestHour = i + 1;
        }
    }

    return bestHour;
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
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)
- [111. Minimum Depth of Binary Tree](../../0001-0500/0111-minimum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-penalty-for-a-shop/)
