# LeetCode 2740: Find the Value of the Partition

**LeetCode Problem #2740 — Find the Value of the Partition**
Solve LeetCode Find the Value of the Partition using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Value of the Partition |
| LeetCode | #2740 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **positive** integer array `nums`.

Partition `nums` into two arrays, `nums1` and `nums2`, such that:

Each element of the array `nums` belongs to either the array `nums1` or the array `nums2`. 
 Both arrays are **non-empty**. 
 The value of the partition is **minimized**.

The value of the partition is `|max(nums1) - min(nums2)|`.

Here, `max(nums1)` denotes the maximum element of the array `nums1`, and `min(nums2)` denotes the minimum element of the array `nums2`.

Return *the integer denoting the value of such partition*.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,3,2,4]`
- **Output:** `1`
- **Explanation:** We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- The maximum element of the array nums1 is equal to 2.
- The minimum element of the array nums2 is equal to 3.
The value of the partition is |2 - 3| = 1. 
It can be proven that 1 is the minimum value out of all partitions.

### Example 2
- **Input:** `nums = [100,1,10]`
- **Output:** `9`
- **Explanation:** We can partition the array nums into nums1 = [10] and nums2 = [100,1].
- The maximum element of the array nums1 is equal to 10.
- The minimum element of the array nums2 is equal to 1.
The value of the partition is |10 - 1| = 9.
It can be proven that 9 is the minimum value out of all partitions.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Value of the Partition**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,4]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- The maximum element of the array nums1 is equal to 2.
- The minimum element of the array nums2 is equal to 3.
The value of the partition is |2 - 3| = 1. 
It can be proven that 1 is the minimum value out of all partitions.

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
var findValueOfPartition = function(nums) {
    nums.sort((a, b) => a - b);

    let minDiff = Infinity;

    for (let i = 1; i < nums.length; i++) {
        let diff = nums[i] - nums[i - 1];

        minDiff = Math.min(minDiff, diff);
    }

    return minDiff;
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
- [513. Find Bottom Left Tree Value](../../0501-1000/0513-find-bottom-left-tree-value/)
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1385-find-the-distance-value-between-two-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-value-of-the-partition/)
