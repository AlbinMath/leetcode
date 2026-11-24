# LeetCode 955: Delete Columns to Make Sorted II

**LeetCode Problem #955 — Delete Columns to Make Sorted II**
Solve LeetCode Delete Columns to Make Sorted II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Columns to Make Sorted II |
| LeetCode | #955 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of `n` strings `strs`, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have `strs = ["abcdef","uvwxyz"]` and deletion indices `{0, 2, 3}`, then the final array after deletions is `["bef", "vyz"]`.

Suppose we chose a set of deletion indices `answer` such that after deletions, the final array has its elements in **lexicographic** order (i.e., `strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]`). Return *the minimum possible value of* `answer.length`.

## Constraints
- `n == strs.length`
- `1 <= n <= 100`
- `1 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `strs = ["ca","bb","ac"]`
- **Output:** `1`
- **Explanation:** After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.

### Example 2
- **Input:** `strs = ["xc","yb","za"]`
- **Output:** `0`
- **Explanation:** strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)

### Example 3
- **Input:** `strs = ["zyx","wvu","tsr"]`
- **Output:** `3`
- **Explanation:** We have to delete every column.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Delete Columns to Make Sorted II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `strs = ["ca","bb","ac"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        settled = [False] * (n - 1)
        deletions = 0

        for c in range(m):
            # does this column violate order for any unsettled pair?
            if any(not settled[i] and strs[i][c] > strs[i + 1][c] for i in range(n - 1)):
                deletions += 1
                continue

            # keep it: settle pairs that are now strictly ordered
            for i in range(n - 1):
                if strs[i][c] < strs[i + 1][c]:
                    settled[i] = True

        return deletions
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
- [944. Delete Columns to Make Sorted](../../0501-1000/0944-delete-columns-to-make-sorted/)
- [960. Delete Columns to Make Sorted III](../../0501-1000/0960-delete-columns-to-make-sorted-iii/)
- [768. Max Chunks To Make Sorted II](../../0501-1000/0768-max-chunks-to-make-sorted-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/)
