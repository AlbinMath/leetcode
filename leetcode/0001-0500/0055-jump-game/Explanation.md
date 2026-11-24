# LeetCode 55: Jump Game

**LeetCode Problem #55 — Jump Game**
Solve LeetCode Jump Game using JavaScript, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game |
| LeetCode | #55 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true`* if you can reach the last index, or *`false`* otherwise*.

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,3,1,1,4]`
- **Output:** `true`
- **Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

### Example 2
- **Input:** `nums = [3,2,1,0,4]`
- **Output:** `false`
- **Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Jump Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,1,1,4]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var canJump = function(nums) {
    let maxReach = 0;

    for (let i = 0; i < nums.length; i++) {
        // Current index is unreachable
        if (i > maxReach) {
            return false;
        }

        // Update the farthest reachable index
        maxReach = Math.max(maxReach, i + nums[i]);

        // The last index is reachable
        if (maxReach >= nums.length - 1) {
            return true;
        }
    }

    return true;
};
```

### Python
```python
class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            # Current index cannot be reached
            if i > farthest:
                return False

            # Update the farthest position we can reach
            farthest = max(farthest, i + nums[i])

            # We can already reach the last index
            if farthest >= len(nums) - 1:
                return True

        return True
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
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [1306. Jump Game III](../../1001-1500/1306-jump-game-iii/)
- [1340. Jump Game V](../../1001-1500/1340-jump-game-v/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game/)
