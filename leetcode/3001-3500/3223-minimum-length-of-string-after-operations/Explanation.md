# LeetCode 3223: Minimum Length of String After Operations

**LeetCode Problem #3223 — Minimum Length of String After Operations**
Solve LeetCode Minimum Length of String After Operations using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Length of String After Operations |
| LeetCode | #3223 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s`.

You can perform the following process on `s` **any** number of times:

Choose an index `i` in the string such that there is **at least** one character to the left of index `i` that is equal to `s[i]`, and **at least** one character to the right that is also equal to `s[i]`. 
 Delete the **closest** occurrence of `s[i]` located to the **left** of `i`. 
 Delete the **closest** occurrence of `s[i]` located to the **right** of `i`.

Return the **minimum** length of the final string `s` that you can achieve.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abaacbcbb"`
- **Output:** `5`
- **Explanation:** We do the following operations: 

 
 Choose index 2, then remove the characters at indices 0 and 3. The resulting string is `s = "bacbcbb"`. 
 Choose index 3, then remove the characters at indices 0 and 5. The resulting string is `s = "acbcb"`.

### Example 2
- **Input:** `s = "aa"`
- **Output:** `2`
- **Explanation:** We cannot perform any operations, so we return the length of the original string.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Length of String After Operations**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abaacbcbb"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** We do the following operations: 

 
 Choose index 2, then remove the characters at indices 0 and 3. The resulting string is `s = "bacbcbb"`. 
 Choose index 3, then remove the characters at indices 0 and 5. The resulting string is `s = "acbcb"`.

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
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        return sum(1 if count % 2 == 1 else 2 for count in freq.values())
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
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1750-minimum-length-of-string-after-deleting-similar-ends/)
- [2696. Minimum String Length After Removing Substrings](../../2501-3000/2696-minimum-string-length-after-removing-substrings/)
- [3746. Minimum String Length After Balanced Removals](../../3501-4000/3746-minimum-string-length-after-balanced-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-length-of-string-after-operations/)
