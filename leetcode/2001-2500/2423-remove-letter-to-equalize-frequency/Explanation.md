# LeetCode 2423: Remove Letter To Equalize Frequency

**LeetCode Problem #2423 — Remove Letter To Equalize Frequency**
Solve LeetCode Remove Letter To Equalize Frequency using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Letter To Equalize Frequency |
| LeetCode | #2423 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** string `word`, consisting of lowercase English letters. You need to select **one** index and **remove** the letter at that index from `word` so that the **frequency** of every letter present in `word` is equal.

Return* *`true`* if it is possible to remove one letter so that the frequency of all letters in *`word`* are equal, and *`false`* otherwise*.

**Note:**

The frequency of a letter `x` is the number of times it occurs in the string. 
 You **must** remove exactly one letter and cannot choose to do nothing.

## Constraints
- `2 <= word.length <= 100`
- `word` consists of lowercase English letters only.

## Examples
### Example 1
- **Input:** `word = "abcc"`
- **Output:** `true`
- **Explanation:** Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

### Example 2
- **Input:** `word = "aazz"`
- **Output:** `false`
- **Explanation:** We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Remove Letter To Equalize Frequency**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "abcc"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

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
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        
        for ch in list(freq.keys()):
            freq[ch] -= 1
            remaining = {count for count in freq.values() if count > 0}
            
            if len(remaining) == 1:
                return True
                
            freq[ch] += 1
            
        return False
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
[View problem on LeetCode](https://leetcode.com/problems/remove-letter-to-equalize-frequency/)
