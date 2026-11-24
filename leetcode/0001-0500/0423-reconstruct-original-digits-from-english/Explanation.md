# LeetCode 423: Reconstruct Original Digits from English

**LeetCode Problem #423 — Reconstruct Original Digits from English**
Solve LeetCode Reconstruct Original Digits from English using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reconstruct Original Digits from English |
| LeetCode | #423 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` containing an out-of-order English representation of digits `0-9`, return *the digits in **ascending** order*.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is one of the characters `["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]`.
- `s` is **guaranteed** to be valid.

## Examples
### Example 1
- **Input:** `s = "owoztneoer"`
- **Output:** `"012"`

### Example 2
- **Input:** `s = "fviefuro"`
- **Output:** `"45"`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Reconstruct Original Digits from English**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "owoztneoer"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"012"`.

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

class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        d = [0] * 10

        # unique letters
        d[0] = c['z']
        d[2] = c['w']
        d[4] = c['u']
        d[6] = c['x']
        d[8] = c['g']

        # identified after removing the above
        d[3] = c['h'] - d[8]
        d[5] = c['f'] - d[4]
        d[7] = c['s'] - d[6]
        d[1] = c['o'] - d[0] - d[2] - d[4]
        d[9] = c['i'] - d[5] - d[6] - d[8]

        return ''.join(str(i) * d[i] for i in range(10))
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
- [332. Reconstruct Itinerary](../../0001-0500/0332-reconstruct-itinerary/)
- [1253. Reconstruct a 2-Row Binary Matrix](../../1001-1500/1253-reconstruct-a-2-row-binary-matrix/)
- [1719. Number Of Ways To Reconstruct A Tree](../../1501-2000/1719-number-of-ways-to-reconstruct-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reconstruct-original-digits-from-english/)
