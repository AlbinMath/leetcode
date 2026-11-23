# LeetCode 47: Permutations II

**LeetCode Problem #47 — Permutations II**
Solve LeetCode Permutations II using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Permutations II |
| LeetCode | #47 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order**.*

## Constraints
- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

## Examples
### Example 1
- **Input:** `nums = [1,1,2]`
- **Output:** `[[1,1,2],
 [1,2,1],
 [2,1,1]]`

### Example 2
- **Input:** `nums = [1,2,3]`
- **Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Permutations II**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,1,2],
 [1,2,1],
 [2,1,1]]`.

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
    def permuteUnique(self, nums):
        nums.sort()
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Skip duplicate choices at the same level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack(path, used)

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
- [46. Permutations](../../0001-0500/0046-permutations/)
- [903. Valid Permutations for DI Sequence](../../0501-1000/0939-valid-permutations-for-di-sequence/)
- [2741. Special Permutations](../../2501-3000/2848-special-permutations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/permutations-ii/)
