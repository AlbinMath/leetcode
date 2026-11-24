# LeetCode 3028: Ant on the Boundary

**LeetCode Problem #3028 — Ant on the Boundary**
Solve LeetCode Ant on the Boundary using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Ant on the Boundary |
| LeetCode | #3028 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An ant is on a boundary. It sometimes goes **left** and sometimes **right**.

You are given an array of **non-zero** integers `nums`. The ant starts reading `nums` from the first element of it to its end. At each step, it moves according to the value of the current element:

If `nums[i] < 0`, it moves **left** by `-nums[i]` units. 
 If `nums[i] > 0`, it moves **right** by `nums[i]` units.

Return *the number of times the ant **returns** to the boundary.*

**Notes:**

There is an infinite space on both sides of the boundary. 
 We check whether the ant is on the boundary only after it has moved `|nums[i]|` units. In other words, if the ant crosses the boundary during its movement, it does not count.

## Constraints
- `1 <= nums.length <= 100`
- `-10 <= nums[i] <= 10`
- `nums[i] != 0`

## Examples
### Example 1
- **Input:** `nums = [2,3,-5]`
- **Output:** `1`
- **Explanation:** After the first step, the ant is 2 steps to the right of the boundary .
After the second step, the ant is 5 steps to the right of the boundary .
After the third step, the ant is on the boundary.
So the answer is 1.

### Example 2
- **Input:** `nums = [3,2,-3,-4]`
- **Output:** `0`
- **Explanation:** After the first step, the ant is 3 steps to the right of the boundary .
After the second step, the ant is 5 steps to the right of the boundary .
After the third step, the ant is 2 steps to the right of the boundary .
After the fourth step, the ant is 2 steps to the left of the boundary .
The ant never returned to the boundary, so the answer is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Ant on the Boundary**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,-5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** After the first step, the ant is 2 steps to the right of the boundary .
After the second step, the ant is 5 steps to the right of the boundary .
After the third step, the ant is on the boundary.
So the answer is 1.

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
var returnToBoundaryCount = function(nums) {
    let position = 0;
    let returns = 0;

    for (const step of nums) {
        position += step;
        if (position === 0) {
            returns++;
        }
    }

    return returns;
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
- [3113. Find the Number of Subarrays Where Boundary Elements Are Maximum](../../3001-3500/3113-find-the-number-of-subarrays-where-boundary-elements-are-maximum/)
- [1916. Count Ways to Build Rooms in an Ant Colony](../../1501-2000/1916-count-ways-to-build-rooms-in-an-ant-colony/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/ant-on-the-boundary/)
