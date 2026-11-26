# LeetCode 1733: Minimum Number of People to Teach

**LeetCode Problem #1733 — Minimum Number of People to Teach**
Solve LeetCode Minimum Number of People to Teach using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of People to Teach |
| LeetCode | #1733 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
On a social network consisting of `m` users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer `n`, an array `languages`, and an array `friendships` where:

There are `n` languages numbered `1` through `n`, 
 `languages[i]` is the set of languages the `i^​​​​​​th`​​​​ user knows, and 
 `friendships[i] = [u_​​​​​​i​​​, v_​​​​​​i]` denotes a friendship between the users `u^​​​​​_​​​​​​i`​​​​​ and `v_i`.

You can choose **one** language and teach it to some users so that all friends can communicate with each other. Return the **minimum** number of users you need to teach.

Note that friendships are not transitive, meaning if `x` is a friend of `y` and `y` is a friend of `z`, this doesn't guarantee that `x` is a friend of `z`.

## Constraints
- `2 <= n <= 500`
- `languages.length == m`
- `1 <= m <= 500`
- `1 <= languages[i].length <= n`
- `1 <= languages[i][j] <= n`
- `1 <= u_​​​​​​i < v_​​​​​​i <= languages.length`
- `1 <= friendships.length <= 500`
- All tuples `(u_​​​​​i, v_​​​​​​i)` are unique
- `languages[i]` contains only unique values

## Examples
### Example 1
- **Input:** `n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]`
- **Output:** `1`
- **Explanation:** You can either teach user 1 the second language or user 2 the first language.

### Example 2
- **Input:** `n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]`
- **Output:** `2`
- **Explanation:** Teach the third language to users 1 and 3, yielding two users to teach.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of People to Teach**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** You can either teach user 1 the second language or user 2 the first language.

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
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_langs = [set(langs) for langs in languages]
        need_help = set()
        for u, v in friendships:
            u_idx, v_idx = u - 1, v - 1
            if user_langs[u_idx].isdisjoint(user_langs[v_idx]):
                need_help.add(u_idx)
                need_help.add(v_idx)
                
        if not need_help:
            return 0
        lang_counts = Counter()
        for user in need_help:
            for lang in user_langs[user]:
                lang_counts[lang] += 1
        max_known = max(lang_counts.values(), default=0)
        return len(need_help) - max_known
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
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-people-to-teach/)
