# LeetCode 46: Permutations

**LeetCode Problem #46 — Permutations**
Solve LeetCode Permutations using JavaScript, Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Permutations |
| LeetCode | #46 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of distinct integers, return all the possible permutations . You can return the answer in **any order**.

## Constraints
- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

### Example 2
- **Input:** `nums = [0,1]`
- **Output:** `[[0,1],[1,0]]`

### Example 3
- **Input:** `nums = [1]`
- **Output:** `[[1]]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Permutations**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var permute = function(nums) {
    const result = [];

    function backtrack(current, used) {
        if (current.length === nums.length) {
            result.push([...current]);
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;

            current.push(nums[i]);
            used[i] = true;

            backtrack(current, used);

            current.pop();
            used[i] = false;
        }
    }

    backtrack([], Array(nums.length).fill(false));

    return result;
};
```

### Python
```python
class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, used):
            # We have selected all numbers
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # Skip numbers already used
                if used[i]:
                    continue

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack(path, used)

                # Undo choice
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [47. Permutations II](../../0001-0500/0047-permutations-ii/)
- [903. Valid Permutations for DI Sequence](../../0501-1000/0939-valid-permutations-for-di-sequence/)
- [2741. Special Permutations](../../2501-3000/2848-special-permutations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/permutations/)
