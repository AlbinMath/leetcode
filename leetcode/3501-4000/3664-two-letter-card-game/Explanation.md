# LeetCode 3664: Two-Letter Card Game

**LeetCode Problem #3664 — Two-Letter Card Game**
Solve LeetCode Two-Letter Card Game using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Two-Letter Card Game |
| LeetCode | #3664 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a deck of cards represented by a string array `cards`, and each card displays two lowercase letters.

You are also given a letter `x`. You play a game with the following rules:

Start with 0 points. 
 On each turn, you must find two **compatible** cards from the deck that both contain the letter `x` in any position. 
 Remove the pair of cards and earn **1 point**. 
 The game ends when you can no longer find a pair of compatible cards.

Return the **maximum** number of points you can gain with optimal play.

Two cards are **compatible** if the strings differ in **exactly** 1 position.

## Constraints
- `2 <= cards.length <= 10^5`
- `cards[i].length == 2`
- Each `cards[i]` is composed of only lowercase English letters between `'a'` and `'j'`.
- `x` is a lowercase English letter between `'a'` and `'j'`.

## Examples
### Example 1
- **Input:** `cards = ["aa","ab","ba","ac"], x = "a"`
- **Output:** `2`
- **Explanation:** On the first turn, select and remove cards `"ab"` and `"ac"`, which are compatible because they differ at only index 1. 
 On the second turn, select and remove cards `"aa"` and `"ba"`, which are compatible because they differ at only index 0. 
 

 Because there are no more compatible pairs, the total score is 2.

### Example 2
- **Input:** `cards = ["aa","ab","ba"], x = "a"`
- **Output:** `1`
- **Explanation:** On the first turn, select and remove cards `"aa"` and `"ba"`. 
 

 Because there are no more compatible pairs, the total score is 1.

### Example 3
- **Input:** `cards = ["aa","ab","ba","ac"], x = "b"`
- **Output:** `0`
- **Explanation:** The only cards that contain the character `'b'` are `"ab"` and `"ba"`. However, they differ in both indices, so they are not compatible. Thus, the output is 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Two-Letter Card Game**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cards = ["aa","ab","ba","ac"], x = "a"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** On the first turn, select and remove cards `"ab"` and `"ac"`, which are compatible because they differ at only index 1. 
 On the second turn, select and remove cards `"aa"` and `"ba"`, which are compatible because they differ at only index 0. 
 

 Because there are no more compatible pairs, the total score is 2.

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
from collections import Counter

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        k = 0
        A, B = Counter(), Counter()
        for c in cards:
            if c == x + x:
                k += 1
            elif c[0] == x:
                A[c[1]] += 1
            elif c[1] == x:
                B[c[0]] += 1

        def solve(cnt):
            s = sum(cnt.values())
            if s == 0:
                return 0, 0
            m = max(cnt.values())
            p = min(s // 2, s - m)
            return p, s - 2 * p

        pa, la = solve(A)
        pb, lb = solve(B)
        pairs = pa + pb
        ans = pairs

        use = min(k, la + lb)       # xx pairs with leftover cards
        ans += use
        k -= use

        ans += min(k // 2, pairs)   # 2 xx break a pair into two pairs
        return ans
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
- [822. Card Flipping Game](../../0501-1000/0822-card-flipping-game/)
- [2131. Longest Palindrome by Concatenating Two Letter Words](../../2001-2500/2131-longest-palindrome-by-concatenating-two-letter-words/)
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/two-letter-card-game/)
