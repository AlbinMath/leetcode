# LeetCode 387: First Unique Character in a String

**LeetCode Problem #387 — First Unique Character in a String**
Solve LeetCode First Unique Character in a String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Unique Character in a String |
| LeetCode | #387 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "leetcode"`
- **Output:** `0`
- **Explanation:** The character `'l'` at index 0 is the first character that does not occur at any other index.

### Example 2
- **Input:** `s = "loveleetcode"`
- **Output:** `2`

### Example 3
- **Input:** `s = "aabb"`
- **Output:** `-1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **First Unique Character in a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leetcode"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The character `'l'` at index 0 is the first character that does not occur at any other index.

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
    def firstUniqChar(self, s):
        count = [0] * 26

        # Count each character
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Find the first character that appears once
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return i

        return -1
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
- [467. Unique Substrings in Wraparound String](../../0001-0500/0467-unique-substrings-in-wraparound-string/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1239-maximum-length-of-a-concatenated-string-with-unique-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)
