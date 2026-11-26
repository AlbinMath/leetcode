# LeetCode 3137: Minimum Number of Operations to Make Word K-Periodic

**LeetCode Problem #3137 — Minimum Number of Operations to Make Word K-Periodic**
Solve LeetCode Minimum Number of Operations to Make Word K-Periodic using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Operations to Make Word K-Periodic |
| LeetCode | #3137 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `word` of size `n`, and an integer `k` such that `k` divides `n`.

In one operation, you can pick any two indices `i` and `j`, that are divisible by `k`, then replace the substring of length `k` starting at `i` with the substring of length `k` starting at `j`. That is, replace the substring `word[i..i + k - 1]` with the substring `word[j..j + k - 1]`.

Return *the **minimum** number of operations required to make* `word` ***k-periodic***.

We say that `word` is **k-periodic** if there is some string `s` of length `k` such that `word` can be obtained by concatenating `s` an arbitrary number of times. For example, if `word == &ldquo;ababab&rdquo;`, then `word` is 2-periodic for `s = "ab"`.

## Constraints
- `1 <= n == word.length <= 10^5`
- `1 <= k <= word.length`
- `k` divides `word.length`.
- `word` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word = "leetcodeleet", k = 4`
- **Output:** `1`
- **Explanation:** We can obtain a 4-periodic string by picking i = 4 and j = 0. After this operation, word becomes equal to "leetleetleet".

### Example 2
- **Input:** `word = " leetcoleet ", k = 2`
- **Output:** `3`
- **Explanation:** We can obtain a 2-periodic string by applying the operations in the table below. 

 
 
 
 i 
 j 
 word 
 
 
 0 
 2 
 etetcoleet 
 
 
 4 
 0 
 etetetleet 
 
 
 6 
 0 
 etetetetet

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Number of Operations to Make Word K-Periodic**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "leetcodeleet", k = 4`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** We can obtain a 4-periodic string by picking i = 4 and j = 0. After this operation, word becomes equal to "leetleetleet".

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
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        block_counts = Counter(word[i : i + k] for i in range(0, n, k))
        
        return (n // k) - max(block_counts.values())
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
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [2111. Minimum Operations to Make the Array K-Increasing](../../2001-2500/2111-minimum-operations-to-make-the-array-k-increasing/)
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3505-minimum-operations-to-make-elements-within-k-subarrays-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/)
