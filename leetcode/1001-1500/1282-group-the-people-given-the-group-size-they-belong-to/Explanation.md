# LeetCode 1282: Group the People Given the Group Size They Belong To

**LeetCode Problem #1282 — Group the People Given the Group Size They Belong To**
Solve LeetCode Group the People Given the Group Size They Belong To using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Group the People Given the Group Size They Belong To |
| LeetCode | #1282 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` people that are split into some unknown number of groups. Each person is labeled with a **unique ID** from `0` to `n - 1`.

You are given an integer array `groupSizes`, where `groupSizes[i]` is the size of the group that person `i` is in. For example, if `groupSizes[1] = 3`, then person `1` must be in a group of size `3`.

Return *a list of groups such that each person `i` is in a group of size `groupSizes[i]`*.

Each person should appear in **exactly one group**, and every person must be in a group. If there are multiple answers, **return any of them**. It is **guaranteed** that there will be **at least one** valid solution for the given input.

## Constraints
- `groupSizes.length == n`
- `1 <= n <= 500`
- `1 <= groupSizes[i] <= n`

## Examples
### Example 1
- **Input:** `groupSizes = [3,3,3,3,3,1,3]`
- **Output:** `[[5],[0,1,2],[3,4,6]]`

### Example 2
- **Input:** `groupSizes = [2,1,3,3,3,2]`
- **Output:** `[[1],[0,5],[2,3,4]]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Group the People Given the Group Size They Belong To**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `groupSizes = [3,3,3,3,3,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[5],[0,1,2],[3,4,6]]`.

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
from collections import defaultdict
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = defaultdict(list)
        result = []
        
        for person_id, size in enumerate(groupSizes):
            buckets[size].append(person_id)
            if len(buckets[size]) == size:
                result.append(buckets[size])
                buckets[size] = []
                
        return result
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
- [1562. Find Latest Group of Size M](../../1501-2000/1562-find-latest-group-of-size-m/)
- [1103. Distribute Candies to People](../../1001-1500/1103-distribute-candies-to-people/)
- [1452. People Whose List of Favorite Companies Is Not a Subset of Another List](../../1001-1500/1452-people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/)
