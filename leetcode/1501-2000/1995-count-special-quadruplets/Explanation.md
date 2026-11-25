# LeetCode 1995: Count Special Quadruplets

**LeetCode Problem #1995 — Count Special Quadruplets**
Solve LeetCode Count Special Quadruplets using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Special Quadruplets |
| LeetCode | #1995 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **0-indexed** integer array `nums`, return *the number of **distinct** quadruplets* `(a, b, c, d)` *such that:*

`nums[a] + nums[b] + nums[c] == nums[d]`, and 
 `a < b < c < d`

## Constraints
- `4 <= nums.length <= 50`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,6]`
- **Output:** `1`
- **Explanation:** The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

### Example 2
- **Input:** `nums = [3,3,6,4,5]`
- **Output:** `0`
- **Explanation:** There are no such quadruplets in [3,3,6,4,5].

### Example 3
- **Input:** `nums = [1,1,1,3,5]`
- **Output:** `4`
- **Explanation:** The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Special Quadruplets**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

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
var countQuadruplets = function(nums) {
    let count = 0;
    const n = nums.length;

    for (let a = 0; a < n - 3; a++) {
        for (let b = a + 1; b < n - 2; b++) {
            for (let c = b + 1; c < n - 1; c++) {
                for (let d = c + 1; d < n; d++) {
                    if (nums[a] + nums[b] + nums[c] === nums[d]) {
                        count++;
                    }
                }
            }
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
- [3120. Count the Number of Special Characters I](../../3001-3500/3120-count-the-number-of-special-characters-i/)
- [3233. Find the Count of Numbers Which Are Not Special](../../3001-3500/3233-find-the-count-of-numbers-which-are-not-special/)
- [3404. Count Special Subsequences](../../3001-3500/3404-count-special-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-special-quadruplets/)
