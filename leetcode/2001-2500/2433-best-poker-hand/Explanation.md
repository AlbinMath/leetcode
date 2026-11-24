# LeetCode 2347: Best Poker Hand

**LeetCode Problem #2347 — Best Poker Hand**
Solve LeetCode Best Poker Hand using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Best Poker Hand |
| LeetCode | #2347 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `ranks` and a character array `suits`. You have `5` cards where the `i^th` card has a rank of `ranks[i]` and a suit of `suits[i]`.

The following are the types of **poker hands** you can make from best to worst:

`"Flush"`: Five cards of the same suit. 
 `"Three of a Kind"`: Three cards of the same rank. 
 `"Pair"`: Two cards of the same rank. 
 `"High Card"`: Any single card.

Return *a string representing the **best** type of **poker hand** you can make with the given cards.*

**Note** that the return values are **case-sensitive**.

## Constraints
- `ranks.length == suits.length == 5`
- `1 <= ranks[i] <= 13`
- `'a' <= suits[i] <= 'd'`
- No two cards have the same rank and suit.

## Examples
### Example 1
- **Input:** `ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]`
- **Output:** `"Flush"`
- **Explanation:** The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".

### Example 2
- **Input:** `ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]`
- **Output:** `"Three of a Kind"`
- **Explanation:** The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a "Three of a Kind".
Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
Also note that other cards could be used to make the "Three of a Kind" hand.

### Example 3
- **Input:** `ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]`
- **Output:** `"Pair"`
- **Explanation:** The hand with the first and second card consists of 2 cards with the same rank, so we have a "Pair".
Note that we cannot make a "Flush" or a "Three of a Kind".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Best Poker Hand**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Flush"`.
4. **Verification:** The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".

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
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
            
        max_freq = max(Counter(ranks).values())
        
        if max_freq >= 3:
            return "Three of a Kind"
        if max_freq == 2:
            return "Pair"
            
        return "High Card"
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
- [121. Best Time to Buy and Sell Stock](../../0001-0500/0121-best-time-to-buy-and-sell-stock/)
- [122. Best Time to Buy and Sell Stock II](../../0001-0500/0122-best-time-to-buy-and-sell-stock-ii/)
- [123. Best Time to Buy and Sell Stock III](../../0001-0500/0123-best-time-to-buy-and-sell-stock-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/best-poker-hand/)
