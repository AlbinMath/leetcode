# LeetCode 198: House Robber

**LeetCode Problem #198 — House Robber**
Solve LeetCode House Robber using JavaScript, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | House Robber |
| LeetCode | #198 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night .

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight without alerting the police *.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,1]`
- **Output:** `4`
- **Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

### Example 2
- **Input:** `nums = [2,7,9,3,1]`
- **Output:** `12`
- **Explanation:** Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **House Robber**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var rob = function(nums) {
    let prev2 = 0;
    let prev1 = 0;

    for (const money of nums) {
        const current = Math.max(
            prev1,
            prev2 + money
        );

        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
};
```

### Python
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for x in nums:
            a, b = b, max(b, a + x)
        return b
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
- [213. House Robber II](../../0001-0500/0213-house-robber-ii/)
- [337. House Robber III](../../0001-0500/0337-house-robber-iii/)
- [2560. House Robber IV](../../2501-3000/2560-house-robber-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/house-robber/)
