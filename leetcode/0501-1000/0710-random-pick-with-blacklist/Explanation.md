# LeetCode 710: Random Pick with Blacklist

**LeetCode Problem #710 — Random Pick with Blacklist**
Solve LeetCode Random Pick with Blacklist using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Random Pick with Blacklist |
| LeetCode | #710 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` and an array of **unique** integers `blacklist`. Design an algorithm to pick a random integer in the range `[0, n - 1]` that is **not** in `blacklist`. Any integer that is in the mentioned range and not in `blacklist` should be **equally likely** to be returned.

Optimize your algorithm such that it minimizes the number of calls to the **built-in** random function of your language.

Implement the `Solution` class:

`Solution(int n, int[] blacklist)` Initializes the object with the integer `n` and the blacklisted integers `blacklist`. 
 `int pick()` Returns a random integer in the range `[0, n - 1]` and not in `blacklist`.

## Constraints
- `1 <= n <= 10^9`
- `0 <= blacklist.length <= min(10^5, n - 1)`
- `0 <= blacklist[i] < n`
- All the values of `blacklist` are **unique**.
- At most `2 * 10^4` calls will be made to `pick`.

## Examples
### Example 1
- **Input:** `["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]`
- **Output:** `[null, 0, 4, 1, 6, 1, 0, 4]`
- **Explanation:** Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
 // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
solution.pick(); // return 4
solution.pick(); // return 1
solution.pick(); // return 6
solution.pick(); // return 1
solution.pick(); // return 0
solution.pick(); // return 4

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Random Pick with Blacklist**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 0, 4, 1, 6, 1, 0, 4]`.
4. **Verification:** Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
 // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
solution.pick(); // return 4
solution.pick(); // return 1
solution.pick(); // return 6
solution.pick(); // return 1
solution.pick(); // return 0
solution.pick(); // return 4

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
import random

class Solution(object):

    def __init__(self, n, blacklist):
        self.m = n - len(blacklist)
        self.mapping = {}
        black_set = set(blacklist)
        
        last = n - 1
        for b in blacklist:
            if b < self.m:
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self):
        r = random.randrange(self.m)
        return self.mapping.get(r, r)
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
- [398. Random Pick Index](../../0001-0500/0398-random-pick-index/)
- [528. Random Pick with Weight](../../0501-1000/0528-random-pick-with-weight/)
- [138. Copy List with Random Pointer](../../0001-0500/0138-copy-list-with-random-pointer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/random-pick-with-blacklist/)
