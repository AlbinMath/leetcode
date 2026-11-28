# LeetCode 944: Delete Columns to Make Sorted

**LeetCode Problem #944 — Delete Columns to Make Sorted**
Solve LeetCode Delete Columns to Make Sorted using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Columns to Make Sorted |
| LeetCode | #944 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of `n` strings `strs`, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

For example, `strs = ["abc", "bce", "cae"]` can be arranged as follows:

abc
bce
cae

You want to **delete** the columns that are **not sorted lexicographically**. In the above example (**0-indexed**), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted, while column 1 (`'b'`, `'c'`, `'a'`) is not, so you would delete column 1.

Return *the number of columns that you will delete*.

## Constraints
- `n == strs.length`
- `1 <= n <= 100`
- `1 <= strs[i].length <= 1000`
- `strs[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `strs = ["cba","daf","ghi"]`
- **Output:** `1`
- **Explanation:** The grid looks as follows:
 cba
 daf
 ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

### Example 2
- **Input:** `strs = ["a","b"]`
- **Output:** `0`
- **Explanation:** The grid looks as follows:
 a
 b
Column 0 is the only column and is sorted, so you will not delete any columns.

### Example 3
- **Input:** `strs = ["zyx","wvu","tsr"]`
- **Output:** `3`
- **Explanation:** The grid looks as follows:
 zyx
 wvu
 tsr
All 3 columns are not sorted, so you will delete all 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Delete Columns to Make Sorted**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `strs = ["cba","daf","ghi"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The grid looks as follows:
 cba
 daf
 ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

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
        rows = len(strs)
        cols = len(strs[0])
        count = 0

        for j in range(cols):
            for i in range(rows - 1):
                if strs[i][j] > strs[i + 1][j]:
                    count += 1
                    break

        return count
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
- [955. Delete Columns to Make Sorted II](../../0501-1000/0955-delete-columns-to-make-sorted-ii/)
- [960. Delete Columns to Make Sorted III](../../0501-1000/0960-delete-columns-to-make-sorted-iii/)
- [1957. Delete Characters to Make Fancy String](../../1501-2000/1957-delete-characters-to-make-fancy-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted/)
