# LeetCode 2971: Find Polygon With the Largest Perimeter

**LeetCode Problem #2971 — Find Polygon With the Largest Perimeter**
Solve LeetCode Find Polygon With the Largest Perimeter using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Polygon With the Largest Perimeter |
| LeetCode | #2971 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of **positive** integers `nums` of length `n`.

A **polygon** is a closed plane figure that has at least `3` sides. The **longest side** of a polygon is **smaller** than the sum of its other sides.

Conversely, if you have `k` (`k >= 3`) **positive** real numbers `a_1`, `a_2`, `a_3`, ..., `a_k` where `a_1 <= a_2 <= a_3 <= ... <= a_k` **and** `a_1 + a_2 + a_3 + ... + a_k-1 > a_k`, then there **always** exists a polygon with `k` sides whose lengths are `a_1`, `a_2`, `a_3`, ..., `a_k`.

The **perimeter** of a polygon is the sum of lengths of its sides.

Return *the **largest** possible **perimeter** of a **polygon** whose sides can be formed from* `nums`, *or* `-1` *if it is not possible to create a polygon*.

## Constraints
- `3 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,5,5]`
- **Output:** `15`
- **Explanation:** The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.

### Example 2
- **Input:** `nums = [1,12,1,2,5,50,3]`
- **Output:** `12`
- **Explanation:** The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12.

### Example 3
- **Input:** `nums = [5,5,50]`
- **Output:** `-1`
- **Explanation:** There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Polygon With the Largest Perimeter**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,5,5]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var largestPerimeter = function(nums) {
    nums.sort((a, b) => a - b);
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }
    for (let i = nums.length - 1; i >= 2; i--) {
        let remainingSum = sum - nums[i];

        if (remainingSum > nums[i]) {
            return sum;
        }
        sum -= nums[i];
    }
    return -1;
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [976. Largest Perimeter Triangle](../../0501-1000/0976-largest-perimeter-triangle/)
- [1738. Find Kth Largest XOR Coordinate Value](../../1501-2000/1738-find-kth-largest-xor-coordinate-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/)
