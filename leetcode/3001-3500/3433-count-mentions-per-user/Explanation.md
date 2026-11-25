# LeetCode 3433: Count Mentions Per User

**LeetCode Problem #3433 — Count Mentions Per User**
Solve LeetCode Count Mentions Per User using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Mentions Per User |
| LeetCode | #3433 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `numberOfUsers` representing the total number of users and an array `events` of size `n x 3`.

Each events[i] can be either of the following two types:

**Message Event:** `["MESSAGE", "timestamp_i", "mentions_string_i"]`

This event indicates that a set of users was mentioned in a message at `timestamp_i`. 
 The `mentions_string_i` string can contain one of the following tokens:
 
 `id<number>`: where `<number>` is an integer in range `[0,numberOfUsers - 1]`. There can be **multiple** ids separated by a single whitespace and may contain duplicates. This can mention even the offline users. 
 `ALL`: mentions **all** users. 
 `HERE`: mentions all **online** users. 
 
 
 
 
 **Offline Event:** `["OFFLINE", "timestamp_i", "id_i"]`
 
 This event indicates that the user `id_i` had become offline at `timestamp_i` for **60 time units**. The user will automatically be online again at time `timestamp_i + 60`.

Return an array `mentions` where `mentions[i]` represents the number of mentions the user with id `i` has across all `MESSAGE` events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed *before* handling any message event that occurs at the same timestamp.

**Note **that a user can be mentioned **multiple** times in a **single** message event, and each mention should be counted **separately**.

## Constraints
- `1 <= numberOfUsers <= 100`
- `1 <= events.length <= 100`
- `events[i].length == 3`
- `events[i][0]` will be one of `MESSAGE` or `OFFLINE`.
- `1 <= int(events[i][1]) <= 10^5`
- The number of `id<number>` mentions in any `"MESSAGE"` event is between `1` and `100`.
- `0 <= <number> <= numberOfUsers - 1`
- It is **guaranteed** that the user id referenced in the `OFFLINE` event is **online** at the time the event occurs.

## Examples
### Example 1
- **Input:** `numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]`
- **Output:** `[2,2]`
- **Explanation:** Initially, all users are online. 

 At timestamp 10, `id1` and `id0` are mentioned. `mentions = [1,1]` 

 At timestamp 11, `id0` goes

### Example 2
- **Input:** `numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]`
- **Output:** `[2,2]`
- **Explanation:** Initially, all users are online. 

 At timestamp 10, `id1` and `id0` are mentioned. `mentions = [1,1]` 

 At timestamp 11, `id0` goes

### Example 3
- **Input:** `numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]`
- **Output:** `[0,1]`
- **Explanation:** Initially, all users are online. 

 At timestamp 10, `id0` goes

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Mentions Per User**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,2]`.
4. **Verification:** Initially, all users are online. 

 At timestamp 10, `id1` and `id0` are mentioned. `mentions = [1,1]` 

 At timestamp 11, `id0` goes

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countMentions = function(numberOfUsers, events) {
    events.sort((a, b) => {
        const tsDiff = Number(a[1]) - Number(b[1]);
        if (tsDiff !== 0) return tsDiff;
        return a[0] === "OFFLINE" ? -1 : 1;
    });

    const mentions = new Array(numberOfUsers).fill(0);
    const onlineAt = new Array(numberOfUsers).fill(0);

    for (const [type, tsStr, payload] of events) {
        const ts = Number(tsStr);
        if (type === "OFFLINE") {
            onlineAt[Number(payload)] = ts + 60;
        } else if (payload === "ALL") {
            for (let u = 0; u < numberOfUsers; u++) {
                mentions[u]++;
            }
        } else if (payload === "HERE") {
            for (let u = 0; u < numberOfUsers; u++) {
                if (onlineAt[u] <= ts) {
                    mentions[u]++;
                }
            }
        } else {
            for (const token of payload.split(" ")) {
                const u = Number(token.slice(2));
                mentions[u]++;
            }
        }
    }

    return mentions;
};
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
- [1348. Tweet Counts Per Frequency](../../1001-1500/1348-tweet-counts-per-frequency/)
- [1661. Average Time of Process per Machine](../../1501-2000/1661-average-time-of-process-per-machine/)
- [38. Count and Say](../../0001-0500/0038-count-and-say/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-mentions-per-user/)
