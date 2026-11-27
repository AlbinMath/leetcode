# LeetCode 3219: Minimum Cost for Cutting Cake II

**LeetCode Problem #3219 — Minimum Cost for Cutting Cake II**
Solve LeetCode Minimum Cost for Cutting Cake II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost for Cutting Cake II |
| LeetCode | #3219 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an `m x n` cake that needs to be cut into `1 x 1` pieces.

You are given integers `m`, `n`, and two arrays:

`horizontalCut` of size `m - 1`, where `horizontalCut[i]` represents the cost to cut along the horizontal line `i`. 
 `verticalCut` of size `n - 1`, where `verticalCut[j]` represents the cost to cut along the vertical line `j`.

In one operation, you can choose any piece of cake that is not yet a `1 x 1` square and perform one of the following cuts:

Cut along a horizontal line `i` at a cost of `horizontalCut[i]`. 
 Cut along a vertical line `j` at a cost of `verticalCut[j]`.

After the cut, the piece of cake is divided into two distinct pieces.

The cost of a cut depends only on the initial cost of the line and does not change.

Return the **minimum** total cost to cut the entire cake into `1 x 1` pieces.

## Constraints
- `1 <= m, n <= 10^5`
- `horizontalCut.length == m - 1`
- `verticalCut.length == n - 1`
- `1 <= horizontalCut[i], verticalCut[i] <= 10^3`

## Examples
### Example 1
- **Input:** `m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]`
- **Output:** `13`
- **Explanation:** Perform a cut on the vertical line 0 with cost 5, current total cost is 5. 
 Perform a cut on the horizontal line 0 on `3 x 1` subgrid with cost 1. 
 Perform a cut on the horizontal line 0 on `3 x 1` subgrid with cost 1. 
 Perform a cut on the horizontal line 1 on `2 x 1` subgrid with cost 3. 
 Perform a cut on the horizontal line 1 on `2 x 1` subgrid with cost 3. 
 

 The total cost is `5 + 1 + 1 + 3 + 3 = 13`.

### Example 2
- **Input:** `m = 2, n = 2, horizontalCut = [7], verticalCut = [4]`
- **Output:** `15`
- **Explanation:** Perform a cut on the horizontal line 0 with cost 7. 
 Perform a cut on the vertical line 0 on `1 x 2` subgrid with cost 4. 
 Perform a cut on the vertical line 0 on `1 x 2` subgrid with cost 4. 
 

 The total cost is `7 + 4 + 4 = 15`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost for Cutting Cake II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** Perform a cut on the vertical line 0 with cost 5, current total cost is 5. 
 Perform a cut on the horizontal line 0 on `3 x 1` subgrid with cost 1. 
 Perform a cut on the horizontal line 0 on `3 x 1` subgrid with cost 1. 
 Perform a cut on the horizontal line 1 on `2 x 1` subgrid with cost 3. 
 Perform a cut on the horizontal line 1 on `2 x 1` subgrid with cost 3. 
 

 The total cost is `5 + 1 + 1 + 3 + 3 = 13`.

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
var minimumCost = function(m, n, horizontalCut, verticalCut) {
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);

    let i = 0;
    let j = 0;

    let horizontalPieces = 1;
    let verticalPieces = 1;

    let totalCost = 0;

    while (i < horizontalCut.length && j < verticalCut.length) {
        if (horizontalCut[i] >= verticalCut[j]) {
            totalCost += horizontalCut[i] * verticalPieces;
            horizontalPieces++;
            i++;
        } else {
            totalCost += verticalCut[j] * horizontalPieces;
            verticalPieces++;
            j++;
        }
    }
    while (i < horizontalCut.length) {
        totalCost += horizontalCut[i] * verticalPieces;
        horizontalPieces++;
        i++;
    }
    while (j < verticalCut.length) {
        totalCost += verticalCut[j] * horizontalPieces;
        verticalPieces++;
        j++;
    }

    return totalCost;
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
- [3218. Minimum Cost for Cutting Cake I](../../3001-3500/3218-minimum-cost-for-cutting-cake-i/)
- [857. Minimum Cost to Hire K Workers](../../0501-1000/0857-minimum-cost-to-hire-k-workers/)
- [983. Minimum Cost For Tickets](../../0501-1000/0983-minimum-cost-for-tickets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/)
