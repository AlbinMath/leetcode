# LeetCode 2862: Maximum Element-Sum of a Complete Subset of Indices

**LeetCode Problem #2862 — Maximum Element-Sum of a Complete Subset of Indices**
Solve LeetCode Maximum Element-Sum of a Complete Subset of Indices using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Element-Sum of a Complete Subset of Indices |
| LeetCode | #2862 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **1****-indexed** array `nums`. Your task is to select a **complete subset** from `nums` where every pair of selected indices multiplied is a perfect square, . i. e. if you select `a_i` and `a_j`, `i * j` must be a perfect square.

Return the *sum* of the complete subset with the *maximum sum*.

## Constraints
- `1 <= n == nums.length <= 10^4`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [8,7,3,5,7,2,4,9]`
- **Output:** `16`
- **Explanation:** We select elements at indices 2 and 8 and `2 * 8` is a perfect square.

### Example 2
- **Input:** `nums = [8,10,3,8,1,13,7,9,4]`
- **Output:** `20`
- **Explanation:** We select elements at indices 1, 4, and 9. `1 * 4`, `1 * 9`, `4 * 9` are perfect squares.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Element-Sum of a Complete Subset of Indices**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [8,7,3,5,7,2,4,9]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** We select elements at indices 2 and 8 and `2 * 8` is a perfect square.

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
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const n = nums.length;
    let maxSum = 0;

    // Try every possible base k (1-indexed)
    for (let k = 1; k <= n; k++) {
        let currentSum = 0;
        
        // Multiply k by consecutive squares: 1^2, 2^2, 3^2, ...
        for (let j = 1; k * j * j <= n; j++) {
            const idx = k * j * j - 1; // Convert 1-indexed to 0-indexed
            currentSum += nums[idx];
        }
        
        if (currentSum > maxSum) {
            maxSum = currentSum;
        }
    }

    return maxSum;
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [918. Maximum Sum Circular Subarray](../../0501-1000/0918-maximum-sum-circular-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/)
