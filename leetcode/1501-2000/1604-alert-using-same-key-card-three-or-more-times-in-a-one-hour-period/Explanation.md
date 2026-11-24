# LeetCode 1604: Alert Using Same Key-Card Three or More Times in a One Hour Period

**LeetCode Problem #1604 — Alert Using Same Key-Card Three or More Times in a One Hour Period**
Solve LeetCode Alert Using Same Key-Card Three or More Times in a One Hour Period using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Alert Using Same Key-Card Three or More Times in a One Hour Period |
| LeetCode | #1604 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an **alert** if any worker uses the key-card **three or more times** in a one-hour period.

You are given a list of strings `keyName` and `keyTime` where `[keyName[i], keyTime[i]]` corresponds to a person's name and the time when their key-card was used **in a** **single day**.

Access times are given in the **24-hour time format "HH:MM"**, such as `"23:51"` and `"09:49"`.

Return a *list of unique worker names who received an alert for frequent keycard use*. Sort the names in **ascending order alphabetically**.

Notice that `"10:00"` - `"11:00"` is considered to be within a one-hour period, while `"22:51"` - `"23:52"` is not considered to be within a one-hour period.

## Constraints
- `1 <= keyName.length, keyTime.length <= 10^5`
- `keyName.length == keyTime.length`
- `keyTime[i]` is in the format **"HH:MM"**.
- `[keyName[i], keyTime[i]]` is **unique**.
- `1 <= keyName[i].length <= 10`
- `keyName[i] contains only lowercase English letters.`

## Examples
### Example 1
- **Input:** `keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]`
- **Output:** `["daniel"]`
- **Explanation:** "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").

### Example 2
- **Input:** `keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]`
- **Output:** `["bob"]`
- **Explanation:** "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Alert Using Same Key-Card Three or More Times in a One Hour Period**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["daniel"]`.
4. **Verification:** "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").

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

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            h, m = t.split(':')
            times[name].append(int(h) * 60 + int(m))

        res = []
        for name, ts in times.items():
            ts.sort()
            for i in range(len(ts) - 2):
                if ts[i + 2] - ts[i] <= 60:
                    res.append(name)
                    break

        return sorted(res)
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
- [1737. Change Minimum Characters to Satisfy One of Three Conditions](../../1501-2000/1737-change-minimum-characters-to-satisfy-one-of-three-conditions/)
- [1566. Detect Pattern of Length M Repeated K or More Times](../../1501-2000/1566-detect-pattern-of-length-m-repeated-k-or-more-times/)
- [1050. Actors and Directors Who Cooperated At Least Three Times](../../1001-1500/1050-actors-and-directors-who-cooperated-at-least-three-times/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)
