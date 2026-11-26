# LeetCode 846: Hand of Straights

**LeetCode Problem #846 — Hand of Straights**
Solve LeetCode Hand of Straights using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Hand of Straights |
| LeetCode | #846 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `i^th` card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

## Constraints
- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

## Examples
### Example 1
- **Input:** `hand = [1,2,3,6,2,3,4,7,8], groupSize = 3`
- **Output:** `true`
- **Explanation:** Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

### Example 2
- **Input:** `hand = [1,2,3,4,5], groupSize = 4`
- **Output:** `false`
- **Explanation:** Alice's hand can not be rearranged into groups of 4.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Hand of Straights**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `hand = [1,2,3,6,2,3,4,7,8], groupSize = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        counts = Counter(hand)
        
        for start in sorted(counts):
            needed = counts[start]
            if needed > 0:
                for card in range(start, start + groupSize):
                    if counts[card] < needed:
                        return False
                    counts[card] -= needed
                    
        return True
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2347. Best Poker Hand](../../2001-2500/2347-best-poker-hand/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/hand-of-straights/)
