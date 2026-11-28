# LeetCode 3301: Maximize the Total Height of Unique Towers

**LeetCode Problem #3301 — Maximize the Total Height of Unique Towers**
Solve LeetCode Maximize the Total Height of Unique Towers using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Total Height of Unique Towers |
| LeetCode | #3301 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `maximumHeight`, where `maximumHeight[i]` denotes the **maximum** height the `i^th` tower can be assigned.

Your task is to assign a height to each tower so that:

The height of the `i^th` tower is a positive integer and does not exceed `maximumHeight[i]`. 
 No two towers have the same height.

Return the **maximum** possible total sum of the tower heights. If it's not possible to assign heights, return `-1`.

## Constraints
- `1 <= maximumHeight.length <= 10^5`
- `1 <= maximumHeight[i] <= 10^9`

## Examples
### Example 1
- **Input:** `maximumHeight = [2,3,4,3]`
- **Output:** `10`
- **Explanation:** We can assign heights in the following way: `[1, 2, 4, 3]`.

### Example 2
- **Input:** `maximumHeight = [15,10]`
- **Output:** `25`
- **Explanation:** We can assign heights in the following way: `[15, 10]`.

### Example 3
- **Input:** `maximumHeight = [2,2,1]`
- **Output:** `-1`
- **Explanation:** It's impossible to assign positive heights to each index so that no two towers have the same height.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize the Total Height of Unique Towers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `maximumHeight = [2,3,4,3]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** We can assign heights in the following way: `[1, 2, 4, 3]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumTotalSum = function(maximumHeight) {
    maximumHeight.sort((a, b) => b - a);

    let totalSum = 0;
    let previousHeight = Infinity;

    for (const maxHeight of maximumHeight) {
        const height = Math.min(maxHeight, previousHeight - 1);
        if (height <= 0) {
            return -1;
        }

        totalSum += height;
        previousHeight = height;
    }

    return totalSum;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2865. Beautiful Towers I](../../2501-3000/2865-beautiful-towers-i/)
- [2866. Beautiful Towers II](../../2501-3000/2866-beautiful-towers-ii/)
- [477. Total Hamming Distance](../../0001-0500/0477-total-hamming-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/)
