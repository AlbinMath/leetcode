# LeetCode 466: Count The Repetitions

**LeetCode Problem #466 — Count The Repetitions**
Solve LeetCode Count The Repetitions using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count The Repetitions |
| LeetCode | #466 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We define `str = [s, n]` as the string `str` which consists of the string `s` concatenated `n` times.

For example, `str == ["abc", 3] =="abcabcabc"`.

We define that string `s1` can be obtained from string `s2` if we can remove some characters from `s2` such that it becomes `s1`.

For example, `s1 = "abc"` can be obtained from `s2 = "ab** dbe **c"` based on our definition by removing the bolded underlined characters.

You are given two strings `s1` and `s2` and two integers `n1` and `n2`. You have the two strings `str1 = [s1, n1]` and `str2 = [s2, n2]`.

Return *the maximum integer *`m`* such that *`str = [str2, m]`* can be obtained from *`str1`.

## Constraints
- `1 <= s1.length, s2.length <= 100`
- `s1` and `s2` consist of lowercase English letters.
- `1 <= n1, n2 <= 10^6`

## Examples
### Example 1
- **Input:** `s1 = "acb", n1 = 4, s2 = "ab", n2 = 2`
- **Output:** `2`

### Example 2
- **Input:** `s1 = "acb", n1 = 1, s2 = "acb", n2 = 1`
- **Output:** `1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count The Repetitions**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "acb", n1 = 4, s2 = "ab", n2 = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        seen = {}          # j -> (i, count) at the start of copy i
        j = 0              # position in s2
        count = 0          # completed s2 copies so far
        i = 0
        extra = 0          # completions gained by skipped cycles
        while i < n1:
            if j in seen and extra == 0:
                pi, pc = seen[j]
                cycle_len = i - pi
                cycle_gain = count - pc
                skips = (n1 - i) // cycle_len
                i += skips * cycle_len
                extra = skips * cycle_gain
                if i >= n1:
                    break
            else:
                seen.setdefault(j, (i, count))
            for c in s1:
                if c == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count += 1
            i += 1
        return (count + extra) // n2
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
- [38. Count and Say](../../0001-0500/0038-count-and-say/)
- [204. Count Primes](../../0001-0500/0204-count-primes/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-repetitions/)
