# LeetCode 40: Combination Sum II

**LeetCode Problem #40 — Combination Sum II**
Solve LeetCode Combination Sum II using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Combination Sum II |
| LeetCode | #40 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

## Constraints
- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Examples
### Example 1
- **Input:** `candidates = [10,1,2,7,6,1,5], target = 8`
- **Output:** `[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]`

### Example 2
- **Input:** `candidates = [2,5,2,1,2], target = 5`
- **Output:** `[
[1,2,2],
[5]
]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Combination Sum II**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `candidates = [10,1,2,7,6,1,5], target = 8`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()
        result = []

        def backtrack(start, current, remaining):

            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate values at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > remaining:
                    break

                # Choose
                current.append(candidates[i])

                # Move to next index because each element
                # can only be used once
                backtrack(i + 1, current, remaining - candidates[i])

                # Undo
                current.pop()

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
- [39. Combination Sum](../../0001-0500/0039-combination-sum/)
- [216. Combination Sum III](../../0001-0500/0216-combination-sum-iii/)
- [377. Combination Sum IV](../../0001-0500/0377-combination-sum-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/combination-sum-ii/)
