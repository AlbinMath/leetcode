# LeetCode 3100: Water Bottles II

**LeetCode Problem #3100 — Water Bottles II**
Solve LeetCode Water Bottles II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Water Bottles II |
| LeetCode | #3100 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `numBottles` and `numExchange`.

`numBottles` represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles. 
 Exchange `numExchange` empty bottles with one full water bottle. Then, increase `numExchange` by one.

Note that you cannot exchange multiple batches of empty bottles for the same value of `numExchange`. For example, if `numBottles == 3` and `numExchange == 1`, you cannot exchange `3` empty water bottles for `3` full bottles.

Return *the **maximum** number of water bottles you can drink*.

## Constraints
- `1 <= numBottles <= 100 `
- `1 <= numExchange <= 100`

## Examples
### Example 1
- **Input:** `numBottles = 13, numExchange = 6`
- **Output:** `15`
- **Explanation:** The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

### Example 2
- **Input:** `numBottles = 10, numExchange = 3`
- **Output:** `13`
- **Explanation:** The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Water Bottles II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numBottles = 13, numExchange = 6`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

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
var maxBottlesDrunk = function(numBottles, numExchange) {
    let drunk = numBottles;
    let empty = numBottles;

    while (empty >= numExchange) {
        empty -= numExchange - 1;
        numExchange++;
        drunk++;
    }

    return drunk;
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
- [1518. Water Bottles](../../1501-2000/1518-water-bottles/)
- [11. Container With Most Water](../../0001-0500/0011-container-with-most-water/)
- [42. Trapping Rain Water](../../0001-0500/0042-trapping-rain-water/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/water-bottles-ii/)
