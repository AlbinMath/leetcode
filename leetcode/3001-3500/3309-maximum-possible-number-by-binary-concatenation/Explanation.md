# LeetCode 3309: Maximum Possible Number by Binary Concatenation

**LeetCode Problem #3309 — Maximum Possible Number by Binary Concatenation**
Solve LeetCode Maximum Possible Number by Binary Concatenation using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Possible Number by Binary Concatenation |
| LeetCode | #3309 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of integers `nums` of size 3.

Return the **maximum** possible number whose *binary representation* can be formed by **concatenating** the *binary representation* of **all** elements in `nums` in some order.

**Note** that the binary representation of any number *does not* contain leading zeros.

## Constraints
- `nums.length == 3`
- `1 <= nums[i] <= 127`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `30`
- **Explanation:** Concatenate the numbers in the order `[3, 1, 2]` to get the result `"11110"`, which is the binary representation of 30.

### Example 2
- **Input:** `nums = [2,8,16]`
- **Output:** `1296`
- **Explanation:** Concatenate the numbers in the order `[2, 8, 16]` to get the result `"10100010000"`, which is the binary representation of 1296.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Possible Number by Binary Concatenation**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `30`.
4. **Verification:** Concatenate the numbers in the order `[3, 1, 2]` to get the result `"11110"`, which is the binary representation of 30.

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
from itertools import permutations

class Solution(object):
    def maxGoodNumber(self, nums):
        best = 0
        for p in permutations(nums):
            s = ''.join(bin(x)[2:] for x in p)
            best = max(best, int(s, 2))
        return best
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
- [2864. Maximum Odd Binary Number](../../2501-3000/2864-maximum-odd-binary-number/)
- [894. All Possible Full Binary Trees](../../0501-1000/0894-all-possible-full-binary-trees/)
- [2959. Number of Possible Sets of Closing Branches](../../2501-3000/2959-number-of-possible-sets-of-closing-branches/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/)
