# LeetCode 884: Uncommon Words from Two Sentences

**LeetCode Problem #884 — Uncommon Words from Two Sentences**
Solve LeetCode Uncommon Words from Two Sentences using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Uncommon Words from Two Sentences |
| LeetCode | #884 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A **sentence** is a string of single-space separated words where each word consists only of lowercase letters.

A word is **uncommon** if it appears exactly once in one of the sentences, and **does not appear** in the other sentence.

Given two **sentences** `s1` and `s2`, return *a list of all the **uncommon words***. You may return the answer in **any order**.

## Constraints
- `1 <= s1.length, s2.length <= 200`
- `s1` and `s2` consist of lowercase English letters and spaces.
- `s1` and `s2` do not have leading or trailing spaces.
- All the words in `s1` and `s2` are separated by a single space.

## Examples
### Example 1
- **Input:** `s1 = "this apple is sweet", s2 = "this apple is sour"`
- **Output:** `["sweet","sour"]`
- **Explanation:** The word `"sweet"` appears only in `s1`, while the word `"sour"` appears only in `s2`.

### Example 2
- **Input:** `s1 = "apple apple", s2 = "banana"`
- **Output:** `["banana"]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Uncommon Words from Two Sentences**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "this apple is sweet", s2 = "this apple is sour"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["sweet","sour"]`.
4. **Verification:** The word `"sweet"` appears only in `s1`, while the word `"sour"` appears only in `s2`.

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
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        count = Counter(words)

        return [word for word in count if count[word] == 1]
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
- [2555. Maximize Win From Two Segments](../../2501-3000/2555-maximize-win-from-two-segments/)
- [2605. Form Smallest Number From Two Digit Arrays](../../2501-3000/2605-form-smallest-number-from-two-digit-arrays/)
- [3981. Count Distinct Ways to Form Target from Two Strings](../../3501-4000/3981-count-distinct-ways-to-form-target-from-two-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/uncommon-words-from-two-sentences/)
