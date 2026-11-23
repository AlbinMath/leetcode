# LeetCode 933: Number of Recent Calls

**LeetCode Problem #933 — Number of Recent Calls**
Solve LeetCode Number of Recent Calls using JavaScript, Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Recent Calls |
| LeetCode | #933 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

`RecentCounter()` Initializes the counter with zero recent requests. 
 `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the inclusive range `[t - 3000, t]`, that is, the new request plus every earlier request that is no more than `3000` milliseconds older.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

## Constraints
- `1 <= t <= 10^9`
- Each test case will call `ping` with **strictly increasing** values of `t`.
- At most `10^4` calls will be made to `ping`.

## Examples
### Example 1
- **Input:** `["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]`
- **Output:** `[null, 1, 2, 3, 3]`
- **Explanation:** RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1); // requests = [ 1 ], range is [-2999,1], return 1
recentCounter.ping(100); // requests = [ 1 , 100 ], range is [-2900,100], return 2
recentCounter.ping(3001); // requests = [ 1 , 100 , 3001 ], range is [1,3001], return 3
recentCounter.ping(3002); // requests = [1, 100 , 3001 , 3002 ], range is [2,3002], return 3

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Recent Calls**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 1, 2, 3, 3]`.
4. **Verification:** RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1); // requests = [ 1 ], range is [-2999,1], return 1
recentCounter.ping(100); // requests = [ 1 , 100 ], range is [-2900,100], return 2
recentCounter.ping(3001); // requests = [ 1 , 100 , 3001 ], range is [1,3001], return 3
recentCounter.ping(3002); // requests = [1, 100 , 3001 , 3002 ], range is [2,3002], return 3

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var RecentCounter = function() {
    this.requests = [];
};

RecentCounter.prototype.ping = function(t) {
    this.requests.push(t);

    while (this.requests[0] < t - 3000) {
        this.requests.shift();
    }

    return this.requests.length;
};
```

### Python
```python
from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)
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
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-recent-calls/)
