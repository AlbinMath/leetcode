# LeetCode 2303: Calculate Amount Paid in Taxes

**LeetCode Problem #2303 — Calculate Amount Paid in Taxes**
Solve LeetCode Calculate Amount Paid in Taxes using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Calculate Amount Paid in Taxes |
| LeetCode | #2303 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** 2D integer array `brackets` where `brackets[i] = [upper_i, percent_i]` means that the `i^th` tax bracket has an upper bound of `upper_i` and is taxed at a rate of `percent_i`. The brackets are **sorted** by upper bound (i.e. `upper_i-1 < upper_i` for `0 < i < brackets.length`).

Tax is calculated as follows:

The first `upper_0` dollars earned are taxed at a rate of `percent_0`. 
 The next `upper_1 - upper_0` dollars earned are taxed at a rate of `percent_1`. 
 The next `upper_2 - upper_1` dollars earned are taxed at a rate of `percent_2`. 
 And so on.

You are given an integer `income` representing the amount of money you earned. Return *the amount of money that you have to pay in taxes.* Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `1 <= brackets.length <= 100`
- `1 <= upper_i <= 1000`
- `0 <= percent_i <= 100`
- `0 <= income <= 1000`
- `upper_i` is sorted in ascending order.
- All the values of `upper_i` are **unique**.
- The upper bound of the last tax bracket is greater than or equal to `income`.

## Examples
### Example 1
- **Input:** `brackets = [[3,50],[7,10],[12,25]], income = 10`
- **Output:** `2.65000`
- **Explanation:** Based on your income, you have 3 dollars in the 1^st tax bracket, 4 dollars in the 2^nd tax bracket, and 3 dollars in the 3^rd tax bracket.
The tax rate for the three tax brackets is 50%, 10%, and 25%, respectively.
In total, you pay $3 * 50% + $4 * 10% + $3 * 25% = $2.65 in taxes.

### Example 2
- **Input:** `brackets = [[1,0],[4,25],[5,50]], income = 2`
- **Output:** `0.25000`
- **Explanation:** Based on your income, you have 1 dollar in the 1^st tax bracket and 1 dollar in the 2^nd tax bracket.
The tax rate for the two tax brackets is 0% and 25%, respectively.
In total, you pay $1 * 0% + $1 * 25% = $0.25 in taxes.

### Example 3
- **Input:** `brackets = [[2,50]], income = 0`
- **Output:** `0.00000`
- **Explanation:** You have no income to tax, so you have to pay a total of $0 in taxes.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Calculate Amount Paid in Taxes**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `brackets = [[3,50],[7,10],[12,25]], income = 10`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2.65000`.
4. **Verification:** Based on your income, you have 3 dollars in the 1^st tax bracket, 4 dollars in the 2^nd tax bracket, and 3 dollars in the 3^rd tax bracket.
The tax rate for the three tax brackets is 50%, 10%, and 25%, respectively.
In total, you pay $3 * 50% + $4 * 10% + $3 * 25% = $2.65 in taxes.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var calculateTax = function(brackets, income) {
    let totalTax = 0;
    let prevUpper = 0;

    for (const [upper, percent] of brackets) {
        if (income <= prevUpper) {
            break;
        }

        const taxable = Math.min(income, upper) - prevUpper;
        totalTax += taxable * (percent / 100);
        prevUpper = upper;
    }

    return totalTax;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2385. Amount of Time for Binary Tree to Be Infected](../../2001-2500/2385-amount-of-time-for-binary-tree-to-be-infected/)
- [2391. Minimum Amount of Time to Collect Garbage](../../2001-2500/2391-minimum-amount-of-time-to-collect-garbage/)
- [3116. Kth Smallest Amount With Single Denomination Combination](../../3001-3500/3116-kth-smallest-amount-with-single-denomination-combination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculate-amount-paid-in-taxes/)
