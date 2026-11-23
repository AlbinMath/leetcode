# LeetCode 2287: Rearrange Characters to Make Target String

**LeetCode Problem #2287 — Rearrange Characters to Make Target String**
Solve LeetCode Rearrange Characters to Make Target String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange Characters to Make Target String |
| LeetCode | #2287 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** strings `s` and `target`. You can take some letters from `s` and rearrange them to form new strings.

Return* the **maximum** number of copies of *`target`* that can be formed by taking letters from *`s`* and rearranging them.*

## Constraints
- `1 <= s.length <= 100`
- `1 <= target.length <= 10`
- `s` and `target` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "ilovecodingonleetcode", target = "code"`
- **Output:** `2`
- **Explanation:** For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
We can make at most two copies of "code", so we return 2.

### Example 2
- **Input:** `s = "abcba", target = "abc"`
- **Output:** `1`
- **Explanation:** We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
We can make at most one copy of "abc", so we return 1.
Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".

### Example 3
- **Input:** `s = "abbaccaddaeea", target = "aaaaa"`
- **Output:** `1`
- **Explanation:** We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
We can make at most one copy of "aaaaa", so we return 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearrange Characters to Make Target String**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ilovecodingonleetcode", target = "code"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
We can make at most two copies of "code", so we return 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        target_counts = Counter(target)
        
        return min(s_counts[ch] // req for ch, req in target_counts.items())
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1957. Delete Characters to Make Fancy String](../../1001-1500/1302-delete-characters-to-make-fancy-string/)
- [1312. Minimum Insertion Steps to Make a String Palindrome](../../1001-1500/1437-minimum-insertion-steps-to-make-a-string-palindrome/)
- [1544. Make The String Great](../../1501-2000/1666-make-the-string-great/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-characters-to-make-target-string/)
