# LeetCode 1803: Count Pairs With XOR in a Range

**LeetCode Problem #1803 — Count Pairs With XOR in a Range**
Solve LeetCode Count Pairs With XOR in a Range using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Pairs With XOR in a Range |
| LeetCode | #1803 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **(0-indexed)** integer array `nums` and two integers `low` and `high`, return *the number of **nice pairs***.

A **nice pair** is a pair `(i, j)` where `0 <= i < j < nums.length` and `low <= (nums[i] XOR nums[j]) <= high`.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i] <= 2 * 10^4`
- `1 <= low <= high <= 2 * 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,4,2,7], low = 2, high = 6`
- **Output:** `6`
- **Explanation:** All nice pairs (i, j) are as follows:
 - (0, 1): nums[0] XOR nums[1] = 5 
 - (0, 2): nums[0] XOR nums[2] = 3
 - (0, 3): nums[0] XOR nums[3] = 6
 - (1, 2): nums[1] XOR nums[2] = 6
 - (1, 3): nums[1] XOR nums[3] = 3
 - (2, 3): nums[2] XOR nums[3] = 5

### Example 2
- **Input:** `nums = [9,8,4,2,1], low = 5, high = 14`
- **Output:** `8`
- **Explanation:** All nice pairs (i, j) are as follows:
​​​​​ - (0, 2): nums[0] XOR nums[2] = 13
 - (0, 3): nums[0] XOR nums[3] = 11
 - (0, 4): nums[0] XOR nums[4] = 8
 - (1, 2): nums[1] XOR nums[2] = 12
 - (1, 3): nums[1] XOR nums[3] = 10
 - (1, 4): nums[1] XOR nums[4] = 9
 - (2, 3): nums[2] XOR nums[3] = 6
 - (2, 4): nums[2] XOR nums[4] = 5

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Pairs With XOR in a Range**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,2,7], low = 2, high = 6`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** All nice pairs (i, j) are as follows:
 - (0, 1): nums[0] XOR nums[1] = 5 
 - (0, 2): nums[0] XOR nums[2] = 3
 - (0, 3): nums[0] XOR nums[3] = 6
 - (1, 2): nums[1] XOR nums[2] = 6
 - (1, 3): nums[1] XOR nums[3] = 3
 - (2, 3): nums[2] XOR nums[3] = 5

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
from typing import List

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        B = 15
        # trie as arrays: children c0, c1 and pass-through counts
        c0, c1, cnt = [0], [0], [0]

        def insert(v):
            node = 0
            for b in range(B - 1, -1, -1):
                if (v >> b) & 1:
                    if not c1[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c1[node] = len(cnt) - 1
                    node = c1[node]
                else:
                    if not c0[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c0[node] = len(cnt) - 1
                    node = c0[node]
                cnt[node] += 1

        def count_less(x, limit):
            # number of inserted y with x ^ y < limit
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                xb = (x >> b) & 1
                lb = (limit >> b) & 1
                if lb:
                    same = c1[node] if xb else c0[node]   # XOR bit 0
                    if same:
                        res += cnt[same]
                    node = c0[node] if xb else c1[node]   # XOR bit 1
                else:
                    node = c1[node] if xb else c0[node]   # XOR bit 0
                if not node:
                    break
            return res

        ans = 0
        for v in nums:
            ans += count_less(v, high + 1) - count_less(v, low)
            insert(v)
        return ans
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
- [327. Count of Range Sum](../../0001-0500/0327-count-of-range-sum/)
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1523-count-odd-numbers-in-an-interval-range/)
- [2586. Count the Number of Vowel Strings in Range](../../2501-3000/2586-count-the-number-of-vowel-strings-in-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/)
