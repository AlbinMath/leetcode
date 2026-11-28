# LeetCode 2747: Count Zero Request Servers

**LeetCode Problem #2747 — Count Zero Request Servers**
Solve LeetCode Count Zero Request Servers using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Zero Request Servers |
| LeetCode | #2747 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` denoting the total number of servers and a **2D** **0-indexed **integer array `logs`, where `logs[i] = [server_id, time]` denotes that the server with id `server_id` received a request at time `time`.

You are also given an integer `x` and a **0-indexed** integer array `queries`.

Return *a **0-indexed** integer array* `arr` *of length* `queries.length` *where* `arr[i]` *represents the number of servers that **did not receive** any requests during the time interval* `[queries[i] - x, queries[i]]`.

Note that the time intervals are inclusive.

## Constraints
- `1 <= n <= 10^5`
- `1 <= logs.length <= 10^5`
- `1 <= queries.length <= 10^5`
- ` logs[i].length == 2 `
- `1 <= logs[i][0] <= n`
- `1 <= logs[i][1] <= 10^6`
- `1 <= x <= 10^5`
- `x < queries[i] <= 10^6`

## Examples
### Example 1
- **Input:** `n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]`
- **Output:** `[1,2]`
- **Explanation:** For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period.

### Example 2
- **Input:** `n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]`
- **Output:** `[0,1]`
- **Explanation:** For queries[0]: All servers get at least one request in the duration of [1, 3].
For queries[1]: Only server with id 3 gets no request in the duration [2,4].

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Zero Request Servers**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period.

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
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        cnt = [0] * (n + 1)
        active = 0
        left = right = 0
        m = len(logs)
        ans = [0] * len(queries)

        for qi in order:
            q = queries[qi]

            # add logs with time <= q
            while right < m and logs[right][1] <= q:
                s = logs[right][0]
                cnt[s] += 1
                if cnt[s] == 1:
                    active += 1
                right += 1

            # remove logs with time < q - x
            while left < m and logs[left][1] < q - x:
                s = logs[left][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                left += 1

            ans[qi] = n - active

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
- [1267. Count Servers that Communicate](../../1001-1500/1267-count-servers-that-communicate/)
- [2169. Count Operations to Obtain Zero](../../2001-2500/2169-count-operations-to-obtain-zero/)
- [38. Count and Say](../../0001-0500/0038-count-and-say/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-zero-request-servers/)
