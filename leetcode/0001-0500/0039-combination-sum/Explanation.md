# LeetCode 39: Combination Sum

**LeetCode Problem #39 — Combination Sum**
Solve LeetCode Combination Sum using JavaScript, Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Combination Sum |
| LeetCode | #39 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of *`candidates`* where the chosen numbers sum to *`target`*.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

## Constraints
- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

## Examples
### Example 1
- **Input:** `candidates = [2,3,6,7], target = 7`
- **Output:** `[[2,2,3],[7]]`
- **Explanation:** 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

### Example 2
- **Input:** `candidates = [2,3,5], target = 8`
- **Output:** `[[2,2,2,2],[2,3,3],[3,5]]`

### Example 3
- **Input:** `candidates = [2], target = 1`
- **Output:** `[]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Combination Sum**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `candidates = [2,3,6,7], target = 7`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[2,2,3],[7]]`.
4. **Verification:** 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

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
var combinationSum = function(candidates, target) {
    const result = [];

    function backtrack(start, current, sum) {
        if (sum === target) {
            result.push([...current]);
            return;
        }

        if (sum > target) {
            return;
        }

        for (let i = start; i < candidates.length; i++) {
            current.push(candidates[i]);

            // Reuse the same candidate by passing i
            backtrack(i, current, sum + candidates[i]);

            current.pop();
        }
    }

    backtrack(0, [], 0);
    return result;
};
```

### Python
```python
class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, current, remaining):

            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return

            # Sum is too large
            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                value = candidates[i]

                # Since candidates are sorted,
                # no later value can work either.
                if value > remaining:
                    break

                # Choose
                current.append(value)

                # We pass i, not i + 1,
                # because the same number can be reused.
                backtrack(i, current, remaining - value)

                # Undo
                current.pop()

        candidates.sort()
        backtrack(0, [], target)

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
- [40. Combination Sum II](../../0001-0500/0040-combination-sum-ii/)
- [216. Combination Sum III](../../0001-0500/0216-combination-sum-iii/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/combination-sum/)
