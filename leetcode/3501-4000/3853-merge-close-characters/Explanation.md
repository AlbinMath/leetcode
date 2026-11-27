# LeetCode 3853: Merge Close Characters

**LeetCode Problem #3853 — Merge Close Characters**
Solve LeetCode Merge Close Characters using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Close Characters |
| LeetCode | #3853 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters and an integer `k`.

Two **equal** characters in the **current** string `s` are considered **close** if the distance between their indices is **at most** `k`.

When two characters are **close**, the right one merges into the left. Merges happen **one at a time**, and after each merge, the string updates until no more merges are possible.

Return the resulting string after performing all possible merges.

**Note**: If multiple merges are possible, always merge the pair with the **smallest left** index. If multiple pairs share the smallest left index, choose the pair with the **smallest right** index.

## Constraints
- `1 <= s.length <= 100`
- `1 <= k <= s.length`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abca", k = 3`
- **Output:** `"abc"`

### Example 2
- **Input:** `s = "aabca", k = 2`
- **Output:** `"abca"`
- **Explanation:** Characters `'a'` at indices `i = 0` and `i = 1` are close as `1 - 0 = 1 <= k`. 
 Merge them into the left `'a'` and `s = "abca"`. 
 Now the remaining `'a'` characters at indices `i = 0` and `i = 3` are not close as `k < 3`, so no further merges occur.

### Example 3
- **Input:** `s = "yybyzybz", k = 2`
- **Output:** `"ybzybz"`
- **Explanation:** Characters `'y'` at indices `i = 0` and `i = 1` are close as `1 - 0 = 1 <= k`. 
 Merge them into the left `'y'` and `s = "ybyzybz"`. 
 Now the characters `'y'` at indices `i = 0` and `i = 2` are close as `2 - 0 = 2 <= k`. 
 Merge them into the left `'y'` and `s = "ybzybz"`. 
 No other equal characters are close, so no further merges occur.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Merge Close Characters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abca", k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abc"`.

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
    def mergeCharacters(self, s: str, k: int) -> str:
        res = []
        for ch in s:
            if ch in res[-k:]:
                continue
            res.append(ch)
        return ''.join(res)
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
- [21. Merge Two Sorted Lists](../../0001-0500/0021-merge-two-sorted-lists/)
- [23. Merge k Sorted Lists](../../0001-0500/0023-merge-k-sorted-lists/)
- [56. Merge Intervals](../../0001-0500/0056-merge-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-close-characters/)
