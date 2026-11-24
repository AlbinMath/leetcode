# LeetCode 914: X of a Kind in a Deck of Cards

**LeetCode Problem #914 — X of a Kind in a Deck of Cards**
Solve LeetCode X of a Kind in a Deck of Cards using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | X of a Kind in a Deck of Cards |
| LeetCode | #914 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `deck` where `deck[i]` represents the number written on the `i^th` card.

Partition the cards into **one or more groups** such that:

Each group has **exactly** `x` cards where `x > 1`, and 
 All the cards in one group have the same integer written on them.

Return `true`* if such partition is possible, or *`false`* otherwise*.

## Constraints
- `1 <= deck.length <= 10^4`
- `0 <= deck[i] < 10^4`

## Examples
### Example 1
- **Input:** `deck = [1,2,3,4,4,3,2,1]`
- **Output:** `true`
- **Explanation:** : Possible partition [1,1],[2,2],[3,3],[4,4].

### Example 2
- **Input:** `deck = [1,1,1,2,2,2,3,3]`
- **Output:** `false`
- **Explanation:** : No possible partition.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **X of a Kind in a Deck of Cards**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `deck = [1,2,3,4,4,3,2,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** : Possible partition [1,1],[2,2],[3,3],[4,4].

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
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck).values()

        return reduce(gcd, counts) >= 2
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
- [1608. Special Array With X Elements Greater Than or Equal X](../../1501-2000/1608-special-array-with-x-elements-greater-than-or-equal-x/)
- [1658. Minimum Operations to Reduce X to Zero](../../1501-2000/1658-minimum-operations-to-reduce-x-to-zero/)
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](../../1501-2000/1779-find-nearest-point-that-has-the-same-x-or-y-coordinate/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)
