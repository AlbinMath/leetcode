# LeetCode 3727: Maximum Alternating Sum of Squares

**LeetCode Problem #3727 — Maximum Alternating Sum of Squares**
Solve LeetCode Maximum Alternating Sum of Squares using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Alternating Sum of Squares |
| LeetCode | #3727 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`. You may **rearrange the elements** in any order.

The **alternating score** of an array `arr` is defined as:

`score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...`

Return an integer denoting the **maximum possible alternating score** of `nums` after rearranging its elements.

## Constraints
- `1 <= nums.length <= 10^5`
- `-4 * 10^4 <= nums[i] <= 4 * 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `12`
- **Explanation:** A possible rearrangement for `nums` is `[2,1,3]`, which gives the maximum alternating score among all possible rearrangements. 

 The alternating score is calculated as: 

 `score = 2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12`

### Example 2
- **Input:** `nums = [1,-1,2,-2,3,-3]`
- **Output:** `16`
- **Explanation:** A possible rearrangement for `nums` is `[-3,-1,-2,1,3,2]`, which gives the maximum alternating score among all possible rearrangements. 

 The alternating score is calculated as: 

 `score = (-3)^2 - (-1)^2 + (-2)^2 - (1)^2 + (3)^2 - (2)^2 = 9 - 1 + 4 - 1 + 9 - 4 = 16`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Alternating Sum of Squares**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** A possible rearrangement for `nums` is `[2,1,3]`, which gives the maximum alternating score among all possible rearrangements. 

 The alternating score is calculated as: 

 `score = 2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12`

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
var maxAlternatingSum = function(nums) {
    const squares = nums
        .map(num => num * num)
        .sort((a, b) => a - b);

    let score = 0;
    const n = squares.length;
    const positiveCount = Math.ceil(n / 2);

    for (let i = 0; i < n; i++) {
        if (i < positiveCount) {
            score += squares[n - 1 - i];
        } else {
            score -= squares[i - positiveCount];
        }
    }

    return score;
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
- [1911. Maximum Alternating Subsequence Sum](../../1501-2000/1911-maximum-alternating-subsequence-sum/)
- [3695. Maximize Alternating Sum Using Swaps](../../3501-4000/3695-maximize-alternating-sum-using-swaps/)
- [3701. Compute Alternating Sum](../../3501-4000/3701-compute-alternating-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)
