# LeetCode 2260: Minimum Consecutive Cards to Pick Up

**LeetCode Problem #2260 — Minimum Consecutive Cards to Pick Up**
Solve LeetCode Minimum Consecutive Cards to Pick Up using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Consecutive Cards to Pick Up |
| LeetCode | #2260 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `cards` where `cards[i]` represents the **value** of the `i^th` card. A pair of cards are **matching** if the cards have the **same** value.

Return* the **minimum** number of **consecutive** cards you have to pick up to have a pair of **matching** cards among the picked cards.* If it is impossible to have matching cards, return `-1`.

## Constraints
- `1 <= cards.length <= 10^5`
- `0 <= cards[i] <= 10^6`

## Examples
### Example 1
- **Input:** `cards = [3,4,2,3,4,7]`
- **Output:** `4`
- **Explanation:** We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

### Example 2
- **Input:** `cards = [1,0,5,3]`
- **Output:** `-1`
- **Explanation:** There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Consecutive Cards to Pick Up**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cards = [3,4,2,3,4,7]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

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
from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        min_len = float('inf')
        
        for i, val in enumerate(cards):
            if val in last_seen:
                length = i - last_seen[val] + 1
                if length == 2:
                    return 2
                if length < min_len:
                    min_len = length
            last_seen[val] = i
            
        return -1 if min_len == float('inf') else min_len
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
- [3086. Minimum Moves to Pick K Ones](../../3001-3500/3327-minimum-moves-to-pick-k-ones/)
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1805-minimum-adjacent-swaps-for-k-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/)
