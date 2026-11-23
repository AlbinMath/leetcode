# LeetCode 3801: Minimum Cost to Merge Sorted Lists

**LeetCode Problem #3801 — Minimum Cost to Merge Sorted Lists**
Solve LeetCode Minimum Cost to Merge Sorted Lists using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Merge Sorted Lists |
| LeetCode | #3801 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `lists`, where each `lists[i]` is a non-empty array of integers **sorted** in **non-decreasing** order.

You may **repeatedly** choose two lists `a = lists[i]` and `b = lists[j]`, where `i != j`, and merge them. The **cost** to merge `a` and `b` is:

`len(a) + len(b) + abs(median(a) - median(b))`, where `len` and `median` denote the list length and median, respectively.

After merging `a` and `b`, remove both `a` and `b` from `lists` and insert the new merged **sorted list** in **any** position. Repeat merges until only **one** list remains.

Return an integer denoting the **minimum total cost** required to merge all lists into one single sorted list.

The **median** of an array is the middle element after sorting it in non-decreasing order. If the array has an even number of elements, the median is the left middle element.

## Constraints
- `2 <= lists.length <= 12`
- `1 <= lists[i].length <= 500`
- `-10^9 <= lists[i][j] <= 10^9`
- `lists[i]` is sorted in non-decreasing order.
- The **sum** of `lists[i].length` will not exceed 2000.

## Examples
### Example 1
- **Input:** `lists = [[1,3,5],[2,4],[6,7,8]]`
- **Output:** `18`
- **Explanation:** Merge `a = [1, 3, 5]` and `b = [2, 4]`: 

 
 `len(a) = 3` and `len(b) = 2` 
 `median(a) = 3` and `median(b) = 2` 
 `cost = len(a) + len(b) + abs(median(a) - median(b)) = 3 + 2 + abs(3 - 2) = 6` 
 

 So `lists` becomes `[[1, 2, 3, 4, 5], [6, 7, 8]]`. 

 Merge `a = [1, 2, 3, 4, 5]` and `b = [6, 7, 8]`: 

 
 `len(a) = 5` and `len(b) = 3` 
 `median(a) = 3` and `median(b) = 7` 
 `cost = len(a) + len(b) + abs(median(a) - median(b)) = 5 + 3 + abs(3 - 7) = 12` 
 

 So `lists` becomes `[[1, 2, 3, 4, 5, 6, 7, 8]]`, and total cost is `6 + 12 = 18`.

### Example 2
- **Input:** `lists = [[1,1,5],[1,4,7,8]]`
- **Output:** `10`
- **Explanation:** Merge `a = [1, 1, 5]` and `b = [1, 4, 7, 8]`: 

 
 `len(a) = 3` and `len(b) = 4` 
 `median(a) = 1` and `median(b) = 4` 
 `cost = len(a) + len(b) + abs(median(a) - median(b)) = 3 + 4 + abs(1 - 4) = 10` 
 

 So `lists` becomes `[[1, 1, 1, 4, 5, 7, 8]]`, and total cost is 10.

### Example 3
- **Input:** `lists = [[1],[3]]`
- **Output:** `4`
- **Explanation:** Merge `a = [1]` and `b = [3]`: 

 
 `len(a) = 1` and `len(b) = 1` 
 `median(a) = 1` and `median(b) = 3` 
 `cost = len(a) + len(b) + abs(median(a) - median(b)) = 1 + 1 + abs(1 - 3) = 4` 
 

 So `lists` becomes `[[1, 3]]`, and total cost is 4.

### Example 4
- **Input:** `lists = [[1],[1]]`
- **Output:** `2`
- **Explanation:** The total cost is `len(a) + len(b) + abs(median(a) - median(b)) = 1 + 1 + abs(1 - 1) = 2`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost to Merge Sorted Lists**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `lists = [[1,3,5],[2,4],[6,7,8]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** Merge `a = [1, 3, 5]` and `b = [2, 4]`: 

 
 `len(a) = 3` and `len(b) = 2` 
 `median(a) = 3` and `median(b) = 2` 
 `cost = len(a) + len(b) + abs(median(a) - median(b)) = 3 + 2 + abs(3 - 2) = 6` 
 

 So `lists` becomes `[[1, 2, 3, 4, 5], [6, 7, 8]]`. 

 Merge `a = [1, 2, 3, 4, 5]` and `b = [6, 7, 8]`: 

 
 `len(a) = 5` and `len(b) = 3` 
 `median(a) = 3` and `median(b) = 7` 
 `cost = len(a) + len(b) + abs(median(a) - median(b)) = 5 + 3 + abs(3 - 7) = 12` 
 

 So `lists` becomes `[[1, 2, 3, 4, 5, 6, 7, 8]]`, and total cost is `6 + 12 = 18`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def minMergeCost(self, lists):
        n = len(lists)
        full = 1 << n
        ln = [0] * full
        med = [0] * full

        for mask in range(1, full):
            merged = []
            for i in range(n):
                if (mask >> i) & 1:
                    merged.extend(lists[i])
            merged.sort()
            ln[mask] = len(merged)
            med[mask] = merged[(len(merged) - 1) // 2]

        INF = float('inf')
        dp = [INF] * full
        for i in range(n):
            dp[1 << i] = 0

        for mask in range(1, full):
            if mask & (mask - 1) == 0:
                continue
            low = mask & -mask
            rest = mask ^ low
            best = INF
            sub = rest
            while True:
                a = sub | low          # part containing the lowest bit
                b = mask ^ a
                if b:
                    c = dp[a] + dp[b] + ln[mask] + abs(med[a] - med[b])
                    if c < best:
                        best = c
                if sub == 0:
                    break
                sub = (sub - 1) & rest
            dp[mask] = best

        return dp[full - 1]
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [21. Merge Two Sorted Lists](../../0001-0500/0021-merge-two-sorted-lists/)
- [23. Merge k Sorted Lists](../../0001-0500/0023-merge-k-sorted-lists/)
- [88. Merge Sorted Array](../../0001-0500/0088-merge-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/)
