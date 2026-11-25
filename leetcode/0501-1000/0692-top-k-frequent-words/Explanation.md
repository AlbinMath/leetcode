# LeetCode 692: Top K Frequent Words

**LeetCode Problem #692 — Top K Frequent Words**
Solve LeetCode Top K Frequent Words using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Top K Frequent Words |
| LeetCode | #692 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of strings `words` and an integer `k`, return *the *`k`* most frequent strings*.

Return the answer **sorted** by **the frequency** from highest to lowest. Sort the words with the same frequency by their **lexicographical order**.

## Constraints
- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `k` is in the range `[1, The number of **unique** words[i]]`

## Examples
### Example 1
- **Input:** `words = ["i","love","leetcode","i","love","coding"], k = 2`
- **Output:** `["i","love"]`
- **Explanation:** "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

### Example 2
- **Input:** `words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4`
- **Output:** `["the","is","sunny","day"]`
- **Explanation:** "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Top K Frequent Words**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["i","love","leetcode","i","love","coding"], k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["i","love"]`.
4. **Verification:** "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

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
import heapq

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        return heapq.nsmallest(k, count, key=lambda w: (-count[w], w))
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
- [347. Top K Frequent Elements](../../0001-0500/0347-top-k-frequent-elements/)
- [508. Most Frequent Subtree Sum](../../0501-1000/0508-most-frequent-subtree-sum/)
- [1838. Frequency of the Most Frequent Element](../../1501-2000/1838-frequency-of-the-most-frequent-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/top-k-frequent-words/)
