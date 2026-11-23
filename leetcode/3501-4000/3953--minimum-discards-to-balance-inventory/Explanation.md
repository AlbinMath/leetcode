# LeetCode 3679:  Minimum Discards to Balance Inventory

**LeetCode Problem #3679 —  Minimum Discards to Balance Inventory**
Solve LeetCode  Minimum Discards to Balance Inventory using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem |  Minimum Discards to Balance Inventory |
| LeetCode | #3679 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `w` and `m`, and an integer array `arrivals`, where `arrivals[i]` is the type of item arriving on day `i` (days are **1-indexed**).

Items are managed according to the following rules:

Each arrival may be **kept** or **discarded**; an item may only be discarded on its arrival day. 
 For each day `i`, consider the window of days `[max(1, i - w + 1), i]` (the `w` most recent days up to day `i`):
 
 For **any** such window, each item type may appear **at most** `m` times among kept arrivals whose arrival day lies in that window. 
 If keeping the arrival on day `i` would cause its type to appear **more than** `m` times in the window, that arrival **must** be discarded.

Return the **minimum** number of arrivals to be discarded so that every `w`-day window contains at most `m` occurrences of each type.

## Constraints
- `1 <= arrivals.length <= 10^5`
- `1 <= arrivals[i] <= 10^5`
- `1 <= w <= arrivals.length`
- `1 <= m <= w`

## Examples
### Example 1
- **Input:** `arrivals = [1,2,1,3,1], w = 4, m = 2`
- **Output:** `0`
- **Explanation:** On day 1, Item 1 arrives; the window contains no more than `m` occurrences of this type, so we keep it. 
 On day 2, Item 2 arrives; the window of days 1 - 2 is fine. 
 On day 3, Item 1 arrives, window `[1, 2, 1]` has item 1 twice, within limit. 
 On day 4, Item 3 arrives, window `[1, 2, 1, 3]` has item 1 twice, allowed. 
 On day 5, Item 1 arrives, window `[2, 1, 3, 1]` has item 1 twice, still valid. 
 

 There are no discarded items, so return 0.

### Example 2
- **Input:** `arrivals = [1,2,3,3,3,4], w = 3, m = 2`
- **Output:** `1`
- **Explanation:** On day 1, Item 1 arrives. We keep it. 
 On day 2, Item 2 arrives, window `[1, 2]` is fine. 
 On day 3, Item 3 arrives, window `[1, 2, 3]` has item 3 once. 
 On day 4, Item 3 arrives, window `[2, 3, 3]` has item 3 twice, allowed. 
 On day 5, Item 3 arrives, window `[3, 3, 3]` has item 3 three times, exceeds limit, so the arrival must be discarded. 
 On day 6, Item 4 arrives, window `[3, 4]` is fine. 
 

 Item 3 on day 5 is discarded, and this is the minimum number of arrivals to discard, so return 1.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve ** Minimum Discards to Balance Inventory**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arrivals = [1,2,1,3,1], w = 4, m = 2`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** On day 1, Item 1 arrives; the window contains no more than `m` occurrences of this type, so we keep it. 
 On day 2, Item 2 arrives; the window of days 1 - 2 is fine. 
 On day 3, Item 1 arrives, window `[1, 2, 1]` has item 1 twice, within limit. 
 On day 4, Item 3 arrives, window `[1, 2, 1, 3]` has item 1 twice, allowed. 
 On day 5, Item 1 arrives, window `[2, 1, 3, 1]` has item 1 twice, still valid. 
 

 There are no discarded items, so return 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List
from collections import defaultdict

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        kept = [False] * len(arrivals)
        ans = 0
        for i, t in enumerate(arrivals):
            j = i - w
            if j >= 0 and kept[j]:
                cnt[arrivals[j]] -= 1
            if cnt[t] >= m:
                ans += 1
            else:
                cnt[t] += 1
                kept[i] = True
        return ans
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [1541. Minimum Insertions to Balance a Parentheses String](../../1501-2000/1648-minimum-insertions-to-balance-a-parentheses-string/)
- [3634. Minimum Removals to Balance Array](../../3501-4000/3958-minimum-removals-to-balance-array/)
- [1382. Balance a Binary Search Tree](../../1001-1500/1285-balance-a-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-discards-to-balance-inventory/)
