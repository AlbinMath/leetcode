# LeetCode 1817: Finding the Users Active Minutes

**LeetCode Problem #1817 — Finding the Users Active Minutes**
Solve LeetCode Finding the Users Active Minutes using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Finding the Users Active Minutes |
| LeetCode | #1817 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given the logs for users' actions on LeetCode, and an integer `k`. The logs are represented by a 2D integer array `logs` where each `logs[i] = [ID_i, time_i]` indicates that the user with `ID_i` performed an action at the minute `time_i`.

**Multiple users** can perform actions simultaneously, and a single user can perform **multiple actions** in the same minute.

The **user active minutes (UAM)** for a given user is defined as the **number of unique minutes** in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a **1-indexed** array `answer` of size `k` such that, for each `j` (`1 <= j <= k`), `answer[j]` is the **number of users** whose **UAM** equals `j`.

Return the array `answer` as described above .

## Constraints
- `1 <= logs.length <= 10^4`
- `0 <= ID_i <= 10^9`
- `1 <= time_i <= 10^5`
- `k` is in the range `[The maximum **UAM** for a user, 10^5]`.

## Examples
### Example 1
- **Input:** `logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5`
- **Output:** `[0,2,0,0,0]`
- **Explanation:** The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.

### Example 2
- **Input:** `logs = [[1,1],[2,2],[2,3]], k = 4`
- **Output:** `[1,1,0,0]`
- **Explanation:** The user with ID=1 performed a single action at minute 1. Hence, they have a UAM of 1.
The user with ID=2 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
There is one user with a UAM of 1 and one with a UAM of 2.
Hence, answer[1] = 1, answer[2] = 1, and the remaining values are 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Finding the Users Active Minutes**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,2,0,0,0]`.
4. **Verification:** The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.

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
from collections import defaultdict
from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = defaultdict(set)
        
        for user_id, minute in logs:
            user_minutes[user_id].add(minute)
            
        answer = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            answer[uam - 1] += 1
            
        return answer
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
- [262. Trips and Users](../../0001-0500/0262-trips-and-users/)
- [1517. Find Users With Valid E-Mails](../../1501-2000/1517-find-users-with-valid-e-mails/)
- [1633. Percentage of Users Attended a Contest](../../1501-2000/1633-percentage-of-users-attended-a-contest/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/finding-the-users-active-minutes/)
