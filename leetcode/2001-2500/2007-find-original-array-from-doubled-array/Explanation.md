# LeetCode 2007: Find Original Array From Doubled Array

**LeetCode Problem #2007 — Find Original Array From Doubled Array**
Solve LeetCode Find Original Array From Doubled Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Original Array From Doubled Array |
| LeetCode | #2007 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An integer array `original` is transformed into a **doubled** array `changed` by appending **twice the value** of every element in `original`, and then randomly **shuffling** the resulting array.

Given an array `changed`, return `original`* if *`changed`* is a **doubled** array. If *`changed`* is not a **doubled** array, return an empty array. The elements in* `original` *may be returned in **any** order*.

## Constraints
- `1 <= changed.length <= 10^5`
- `0 <= changed[i] <= 10^5`

## Examples
### Example 1
- **Input:** `changed = [1,3,4,2,6,8]`
- **Output:** `[1,3,4]`
- **Explanation:** One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

### Example 2
- **Input:** `changed = [6,3,0,1]`
- **Output:** `[]`
- **Explanation:** changed is not a doubled array.

### Example 3
- **Input:** `changed = [1]`
- **Output:** `[]`
- **Explanation:** changed is not a doubled array.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Original Array From Doubled Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `changed = [1,3,4,2,6,8]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,4]`.
4. **Verification:** One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        cnt = Counter(changed)
        res = []
        for x in sorted(cnt):
            if cnt[x] == 0:
                continue
            if x == 0:
                if cnt[0] % 2:
                    return []
                res.extend([0] * (cnt[0] // 2))
                cnt[0] = 0
                continue
            if cnt[2 * x] < cnt[x]:
                return []
            res.extend([x] * cnt[x])
            cnt[2 * x] -= cnt[x]
            cnt[x] = 0
        return res
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2433. Find The Original Array of Prefix Xor](../../2001-2500/2433-find-the-original-array-of-prefix-xor/)
- [423. Reconstruct Original Digits from English](../../0001-0500/0423-reconstruct-original-digits-from-english/)
- [2122. Recover the Original Array](../../2001-2500/2122-recover-the-original-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-original-array-from-doubled-array/)
