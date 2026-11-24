# LeetCode 825: Friends Of Appropriate Ages

**LeetCode Problem #825 — Friends Of Appropriate Ages**
Solve LeetCode Friends Of Appropriate Ages using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Friends Of Appropriate Ages |
| LeetCode | #825 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` persons on a social media website. You are given an integer array `ages` where `ages[i]` is the age of the `i^th` person.

A Person `x` will not send a friend request to a person `y` (`x != y`) if any of the following conditions is true:

`age[y] <= 0.5 * age[x] + 7` 
 `age[y] > age[x]` 
 `age[y] > 100 && age[x] < 100`

Otherwise, `x` will send a friend request to `y`.

Note that if `x` sends a request to `y`, `y` will not necessarily send a request to `x`. Also, a person will not send a friend request to themself.

Return *the total number of friend requests made*.

## Constraints
- `n == ages.length`
- `1 <= n <= 2 * 10^4`
- `1 <= ages[i] <= 120`

## Examples
### Example 1
- **Input:** `ages = [16,16]`
- **Output:** `2`
- **Explanation:** 2 people friend request each other.

### Example 2
- **Input:** `ages = [16,17,18]`
- **Output:** `2`
- **Explanation:** Friend requests are made 17 -> 16, 18 -> 17.

### Example 3
- **Input:** `ages = [20,30,100,110,120]`
- **Output:** `3`
- **Explanation:** Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Friends Of Appropriate Ages**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `ages = [16,16]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** 2 people friend request each other.

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
from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for a in ages:
            cnt[a] += 1

        total = 0
        for a in range(1, 121):
            if cnt[a] == 0:
                continue
            for b in range(a // 2 + 8, a + 1):
                total += cnt[a] * cnt[b]
                if a == b:
                    total -= cnt[a]

        return total
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
- [602. Friend Requests II: Who Has the Most Friends](../../0501-1000/0602-friend-requests-ii-who-has-the-most-friends/)
- [1311. Get Watched Videos by Your Friends](../../1001-1500/1311-get-watched-videos-by-your-friends/)
- [1583. Count Unhappy Friends](../../1501-2000/1583-count-unhappy-friends/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/friends-of-appropriate-ages/)
