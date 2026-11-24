# LeetCode 1079: Letter Tile Possibilities

**LeetCode Problem #1079 — Letter Tile Possibilities**
Solve LeetCode Letter Tile Possibilities using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Letter Tile Possibilities |
| LeetCode | #1079 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have `n` `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return *the number of possible non-empty sequences of letters* you can make using the letters printed on those `tiles`.

## Constraints
- `1 <= tiles.length <= 7`
- `tiles` consists of uppercase English letters.

## Examples
### Example 1
- **Input:** `tiles = "AAB"`
- **Output:** `8`
- **Explanation:** The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

### Example 2
- **Input:** `tiles = "AAABBC"`
- **Output:** `188`

### Example 3
- **Input:** `tiles = "V"`
- **Output:** `1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Letter Tile Possibilities**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tiles = "AAB"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

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
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)

        def dfs() -> int:
            total = 0
            for ch in cnt:
                if cnt[ch] == 0:
                    continue
                cnt[ch] -= 1
                total += 1 + dfs()  # 1 for the sequence ending here
                cnt[ch] += 1
            return total

        return dfs()
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
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0744-find-smallest-letter-greater-than-target/)
- [784. Letter Case Permutation](../../0501-1000/0784-letter-case-permutation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/letter-tile-possibilities/)
