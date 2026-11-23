# LeetCode 3325: Count Substrings With K-Frequency Characters I

**LeetCode Problem #3325 — Count Substrings With K-Frequency Characters I**
Solve LeetCode Count Substrings With K-Frequency Characters I using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Substrings With K-Frequency Characters I |
| LeetCode | #3325 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` and an integer `k`, return the total number of substrings of `s` where **at least one** character appears **at least** `k` times.

## Constraints
- `1 <= s.length <= 3000`
- `1 <= k <= s.length`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abacb", k = 2`
- **Output:** `4`
- **Explanation:** The valid substrings are: 

 
 `"aba"` (character `'a'` appears 2 times). 
 `"abac"` (character `'a'` appears 2 times). 
 `"abacb"` (character `'a'` appears 2 times). 
 `"bacb"` (character `'b'` appears 2 times).

### Example 2
- **Input:** `s = "abcde", k = 1`
- **Output:** `15`
- **Explanation:** All substrings are valid because every character appears at least once.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Substrings With K-Frequency Characters I**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abacb", k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The valid substrings are: 

 
 `"aba"` (character `'a'` appears 2 times). 
 `"abac"` (character `'a'` appears 2 times). 
 `"abacb"` (character `'a'` appears 2 times). 
 `"bacb"` (character `'b'` appears 2 times).

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
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = [0] * 26
        l = 0
        ans = 0
        for ch in s:
            c = ord(ch) - 97
            cnt[c] += 1
            while cnt[c] >= k:
                cnt[ord(s[l]) - 97] -= 1
                l += 1
            ans += l
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0855-count-unique-characters-of-all-substrings-of-a-given-string/)
- [3258. Count Substrings That Satisfy K-Constraint I](../../3501-4000/3543-count-substrings-that-satisfy-k-constraint-i/)
- [3261. Count Substrings That Satisfy K-Constraint II](../../3501-4000/3546-count-substrings-that-satisfy-k-constraint-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/)
