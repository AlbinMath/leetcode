# LeetCode 1481: Least Number of Unique Integers after K Removals

**LeetCode Problem #1481 — Least Number of Unique Integers after K Removals**
Solve LeetCode Least Number of Unique Integers after K Removals using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Least Number of Unique Integers after K Removals |
| LeetCode | #1481 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr` and an integer `k`. Find the *least number of unique integers* after removing **exactly** `k` elements .

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^9`
- `0 <= k <= arr.length`

## Examples
### Example 1
- **Input:** `arr = [5,5,4], k = 1`
- **Output:** `1`
- **Explanation:** : Remove the single 4, only 5 is left.

### Example 2
- **Input:** `arr = [4,3,1,1,3,3,2], k = 3`
- **Output:** `2`
- **Explanation:** : Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Least Number of Unique Integers after K Removals**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [5,5,4], k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** : Remove the single 4, only 5 is left.

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
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freqs = sorted(Counter(arr).values())
        unique = len(freqs)
        for f in freqs:
            if k >= f:
                k -= f
                unique -= 1
            else:
                break
        return unique
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
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2477-number-of-ways-to-reach-a-position-after-exactly-k-steps/)
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2501-3000/2525-count-number-of-distinct-integers-after-reverse-operations/)
- [3621. Number of Integers With Popcount-Depth Equal to K I](../../3501-4000/3937-number-of-integers-with-popcount-depth-equal-to-k-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/)
