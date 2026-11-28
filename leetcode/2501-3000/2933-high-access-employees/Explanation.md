# LeetCode 2933: High-Access Employees

**LeetCode Problem #2933 — High-Access Employees**
Solve LeetCode High-Access Employees using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | High-Access Employees |
| LeetCode | #2933 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D **0-indexed** array of strings, `access_times`, with size `n`. For each `i` where `0 <= i <= n - 1`, `access_times[i][0]` represents the name of an employee, and `access_times[i][1]` represents the access time of that employee. All entries in `access_times` are within the same day.

The access time is represented as **four digits** using a **24-hour** time format, for example, `"0800"` or `"2250"`.

An employee is said to be **high-access** if he has accessed the system **three or more** times within a **one-hour period**.

Times with exactly one hour of difference are **not** considered part of the same one-hour period. For example, `"0815"` and `"0915"` are not part of the same one-hour period.

Access times at the start and end of the day are **not** counted within the same one-hour period. For example, `"0005"` and `"2350"` are not part of the same one-hour period.

Return *a list that contains the names of **high-access** employees with any order you want.*

## Constraints
- `1 <= access_times.length <= 100`
- `access_times[i].length == 2`
- `1 <= access_times[i][0].length <= 10`
- `access_times[i][0]` consists only of English small letters.
- `access_times[i][1].length == 4`
- `access_times[i][1]` is in 24-hour time format.
- `access_times[i][1]` consists only of `'0'` to `'9'`.

## Examples
### Example 1
- **Input:** `access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]`
- **Output:** `["a"]`
- **Explanation:** "a" has three access times in the one-hour period of [05:32, 06:31] which are 05:32, 05:49, and 06:21.
But "b" does not have more than two access times at all.
So the answer is ["a"].

### Example 2
- **Input:** `access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]`
- **Output:** `["c","d"]`
- **Explanation:** "c" has three access times in the one-hour period of [08:08, 09:07] which are 08:08, 08:09, and 08:29.
"d" has also three access times in the one-hour period of [14:10, 15:09] which are 14:10, 14:44, and 15:08.
However, "e" has just one access time, so it can not be in the answer and the final answer is ["c","d"].

### Example 3
- **Input:** `access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]`
- **Output:** `["ab","cd"]`
- **Explanation:** "ab" has three access times in the one-hour period of [10:25, 11:24] which are 10:25, 11:20, and 11:24.
"cd" has also three access times in the one-hour period of [10:25, 11:24] which are 10:25, 10:46, and 10:55.
So the answer is ["ab","cd"].

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **High-Access Employees**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["a"]`.
4. **Verification:** "a" has three access times in the one-hour period of [05:32, 06:31] which are 05:32, 05:49, and 06:21.
But "b" does not have more than two access times at all.
So the answer is ["a"].

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
var findHighAccessEmployees = function(access_times) {
    const map = new Map();
    const result = [];
    for (const [name, time] of access_times) {
        const hours = Number(time.slice(0, 2));
        const minutes = Number(time.slice(2, 4));

        const totalMinutes = hours * 60 + minutes;

        if (!map.has(name)) {
            map.set(name, []);
        }
        map.get(name).push(totalMinutes);
    }
    for (const [name, times] of map) {
        times.sort((a, b) => a - b);

        for (let i = 0; i + 2 < times.length; i++) {
            if (times[i + 2] - times[i] < 60) {
                result.push(name);
                break;
            }
        }
    }
    return result;
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
- [181. Employees Earning More Than Their Managers](../../0001-0500/0181-employees-earning-more-than-their-managers/)
- [627. Swap Sex of Employees](../../0501-1000/0627-swap-sex-of-employees/)
- [1075. Project Employees I](../../1001-1500/1075-project-employees-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/high-access-employees/)
