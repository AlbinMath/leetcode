# LeetCode 3074: Apple Redistribution into Boxes

**LeetCode Problem #3074 — Apple Redistribution into Boxes**
Solve LeetCode Apple Redistribution into Boxes using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apple Redistribution into Boxes |
| LeetCode | #3074 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `apple` of size `n` and an array `capacity` of size `m`.

There are `n` packs where the `i^th` pack contains `apple[i]` apples. There are `m` boxes as well, and the `i^th` box has a capacity of `capacity[i]` apples.

Return *the **minimum** number of boxes you need to select to redistribute these *`n`* packs of apples into boxes*.

**Note** that, apples from the same pack can be distributed into different boxes.

## Constraints
- `1 <= n == apple.length <= 50`
- `1 <= m == capacity.length <= 50`
- `1 <= apple[i], capacity[i] <= 50`
- The input is generated such that it's possible to redistribute packs of apples into boxes.

## Examples
### Example 1
- **Input:** `apple = [1,3,2], capacity = [4,3,1,5,2]`
- **Output:** `2`
- **Explanation:** We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.

### Example 2
- **Input:** `apple = [5,5,5], capacity = [2,4,2,7]`
- **Output:** `4`
- **Explanation:** We will need to use all the boxes.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Apple Redistribution into Boxes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `apple = [1,3,2], capacity = [4,3,1,5,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.

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
var minimumBoxes = function(apple, capacity) {
    let totalApples = apple.reduce((sum, x) => sum + x, 0);
    capacity.sort((a, b) => b - a);

    let count = 0;
    for (let cap of capacity) {
        totalApples -= cap;
        count++;

        if (totalApples <= 0) {
            return count;
        }
    }

    return count;
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
- [659. Split Array into Consecutive Subsequences](../../0501-1000/0659-split-array-into-consecutive-subsequences/)
- [701. Insert into a Binary Search Tree](../../0501-1000/0701-insert-into-a-binary-search-tree/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0842-split-array-into-fibonacci-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apple-redistribution-into-boxes/)
