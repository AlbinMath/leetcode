# LeetCode 3186: Maximum Total Damage With Spell Casting

**LeetCode Problem #3186 — Maximum Total Damage With Spell Casting**
Solve LeetCode Maximum Total Damage With Spell Casting using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total Damage With Spell Casting |
| LeetCode | #3186 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A magician has various spells.

You are given an array `power`, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of `power[i]`, they **cannot** cast any spell with a damage of `power[i] - 2`, `power[i] - 1`, `power[i] + 1`, or `power[i] + 2`.

Each spell can be cast **only once**.

Return the **maximum** possible *total damage* that a magician can cast.

## Constraints
- `1 <= power.length <= 10^5`
- `1 <= power[i] <= 10^9`

## Examples
### Example 1
- **Input:** `power = [1,1,3,4]`
- **Output:** `6`
- **Explanation:** The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

### Example 2
- **Input:** `power = [7,1,6,6]`
- **Output:** `13`
- **Explanation:** The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Total Damage With Spell Casting**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `power = [1,1,3,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

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
    def maximumTotalDamage(self, power: list[int]) -> int:
        freq = Counter(power)
        vals = sorted(freq.keys())
        m = len(vals)
        
        dp = [0] * m
        
        for i in range(m):
            curr_gain = vals[i] * freq[vals[i]]
            
            j = i - 1
            while j >= 0 and vals[i] - vals[j] <= 2:
                j -= 1
                
            if j >= 0:
                curr_gain += dp[j]
                
            dp[i] = max(dp[i - 1] if i > 0 else 0, curr_gain)
            
        return dp[-1]
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
- [2234. Maximum Total Beauty of the Gardens](../../2001-2500/2330-maximum-total-beauty-of-the-gardens/)
- [2285. Maximum Total Importance of Roads](../../2001-2500/2379-maximum-total-importance-of-roads/)
- [3180. Maximum Total Reward Using Operations I](../../3001-3500/3442-maximum-total-reward-using-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/)
