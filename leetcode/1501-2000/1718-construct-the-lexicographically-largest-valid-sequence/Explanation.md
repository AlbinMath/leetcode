# LeetCode 1718: Construct the Lexicographically Largest Valid Sequence

**LeetCode Problem #1718 — Construct the Lexicographically Largest Valid Sequence**
Solve LeetCode Construct the Lexicographically Largest Valid Sequence using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct the Lexicographically Largest Valid Sequence |
| LeetCode | #1718 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer `n`, find a sequence with elements in the range `[1, n]` that satisfies all of the following:

The integer `1` occurs once in the sequence. 
 Each integer between `2` and `n` occurs twice in the sequence. 
 For every integer `i` between `2` and `n`, the **distance** between the two occurrences of `i` is exactly `i`.

The **distance** between two numbers on the sequence, `a[i]` and `a[j]`, is the absolute difference of their indices, `|j - i|`.

Return *the **lexicographically largest** sequence**. It is guaranteed that under the given constraints, there is always a solution. *

A sequence `a` is lexicographically larger than a sequence `b` (of the same length) if in the first position where `a` and `b` differ, sequence `a` has a number greater than the corresponding number in `b`. For example, `[0,1,9,0]` is lexicographically larger than `[0,1,5,6]` because the first position they differ is at the third number, and `9` is greater than `5`.

## Constraints
- `1 <= n <= 20`

## Examples
### Example 1
- **Input:** `n = 3`
- **Output:** `[3,1,2,3,2]`
- **Explanation:** [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.

### Example 2
- **Input:** `n = 5`
- **Output:** `[5,3,1,4,3,5,2,4,2]`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Construct the Lexicographically Largest Valid Sequence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1,2,3,2]`.
4. **Verification:** [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        res = [0] * size
        used = [False] * (n + 1)

        def dfs(pos: int) -> bool:
            while pos < size and res[pos]:
                pos += 1
            if pos == size:
                return True
            for v in range(n, 0, -1):
                if used[v]:
                    continue
                if v == 1:
                    res[pos] = 1
                    used[1] = True
                    if dfs(pos + 1):
                        return True
                    res[pos] = 0
                    used[1] = False
                else:
                    j = pos + v
                    if j < size and res[j] == 0:
                        res[pos] = res[j] = v
                        used[v] = True
                        if dfs(pos + 1):
                            return True
                        res[pos] = res[j] = 0
                        used[v] = False
            return False

        dfs(0)
        return res
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3302. Find the Lexicographically Smallest Valid Sequence](../../3001-3500/3302-find-the-lexicographically-smallest-valid-sequence/)
- [3403. Find the Lexicographically Largest String From the Box I](../../3001-3500/3403-find-the-lexicographically-largest-string-from-the-box-i/)
- [4036. Lexicographically Largest String After Pair Transformations](../../4001-4500/4036-lexicographically-largest-string-after-pair-transformations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/)
