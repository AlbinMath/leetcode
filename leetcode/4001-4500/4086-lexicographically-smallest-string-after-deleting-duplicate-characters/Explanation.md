# LeetCode 3816: Lexicographically Smallest String After Deleting Duplicate Characters

**LeetCode Problem #3816 — Lexicographically Smallest String After Deleting Duplicate Characters**
Solve LeetCode Lexicographically Smallest String After Deleting Duplicate Characters using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest String After Deleting Duplicate Characters |
| LeetCode | #3816 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` that consists of lowercase English letters.

You can perform the following operation any number of times (possibly zero times):

Choose any letter that appears **at least twice** in the current string `s` and delete any **one** occurrence.

Return the ** lexicographically smallest ** resulting string that can be formed this way.

## Constraints
- `1 <= s.length <= 10^5`
- `s` contains lowercase English letters only.

## Examples
### Example 1
- **Input:** `s = "aaccb"`
- **Output:** `"aacb"`
- **Explanation:** We can form the strings `"acb"`, `"aacb"`, `"accb"`, and `"aaccb"`. `"aacb"` is the lexicographically smallest one. 

 For example, we can obtain `"aacb"` by choosing `'c'` and deleting its first occurrence.

### Example 2
- **Input:** `s = "z"`
- **Output:** `"z"`
- **Explanation:** We cannot perform any operations. The only string we can form is `"z"`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Lexicographically Smallest String After Deleting Duplicate Characters**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaccb"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"aacb"`.
4. **Verification:** We can form the strings `"acb"`, `"aacb"`, `"accb"`, and `"aaccb"`. `"aacb"` is the lexicographically smallest one. 

 For example, we can obtain `"aacb"` by choosing `'c'` and deleting its first occurrence.

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
    def lexSmallestAfterDeletion(self, s: str) -> str:
        total = Counter(s)
        stack = []
        for c in s:
            while stack and stack[-1] > c and total[stack[-1]] > 1:
                total[stack.pop()] -= 1
            stack.append(c)

        while stack and total[stack[-1]] > 1:
            total[stack.pop()] -= 1

        return ''.join(stack)
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
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1747-lexicographically-smallest-string-after-applying-operations/)
- [3722. Lexicographically Smallest String After Reverse](../../4001-4500/4073-lexicographically-smallest-string-after-reverse/)
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1058-lexicographically-smallest-equivalent-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/)
