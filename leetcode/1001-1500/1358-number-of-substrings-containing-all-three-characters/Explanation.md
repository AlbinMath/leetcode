# LeetCode 1358: Number of Substrings Containing All Three Characters

**LeetCode Problem #1358 — Number of Substrings Containing All Three Characters**
Solve LeetCode Number of Substrings Containing All Three Characters using Java, Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Substrings Containing All Three Characters |
| LeetCode | #1358 |
| Difficulty | Medium |
| Language | Java, Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` consisting only of characters *a*, *b* and *c*.

Return the number of substrings containing at least one occurrence of all these characters *a*, *b* and *c*.

## Constraints
- `3 <= s.length <= 5 x 10^4`
- `s` only consists of `'a'`, `'b'` or `'c'` characters.

## Examples
### Example 1
- **Input:** `s = "abcabc"`
- **Output:** `10`
- **Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are "*abc*", "*abca*", "*abcab*", "*abcabc*", "*bca*", "*bcab*", "*bcabc*", "*cab*", "*cabc*" *and* "*abc*" *(

### Example 2
- **Input:** `s = "aaacb"`
- **Output:** `3`
- **Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are "*aaacb*", "*aacb*" *and* "*acb*".** *

### Example 3
- **Input:** `s = "abc"`
- **Output:** `1`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a clever **counting approach** based on tracking the last occurrence of each character.

1. **Last Array:** `last[0]`, `last[1]`, `last[2]` store the most recent index where `a`, `b`, `c` appeared, initialized to `-1`.
2. For each index `right`, update `last[s[right] - 'a'] = right`.
3. If all three characters have appeared (`last[0] != -1 && last[1] != -1 && last[2] != -1`):
   - Find `minLast` = the earliest of the three last positions. Any substring starting from index `0` through `minLast` (inclusive) and ending at `right` will contain all three characters.
   - Add `minLast + 1` to the answer.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcabc"`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are "*abc*", "*abca*", "*abcab*", "*abcabc*", "*bca*", "*bcab*", "*bcabc*", "*cab*", "*cabc*" *and* "*abc*" *(

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Java, Python

## Source Code
- [solution.java](./solution.java)
- [solution.py](./solution.py)


### Java
```java
class Solution {
    public int numberOfSubstrings(String s) {
        int[] last = {-1, -1, -1};
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {
            int index = s.charAt(right) - 'a';
            last[index] = right;

            // All three characters have appeared
            if (last[0] != -1 && last[1] != -1 && last[2] != -1) {
                int minLast = Math.min(last[0],
                              Math.min(last[1], last[2]));

                ans += minLast + 1;
            }
        }

        return ans;
    }
}
```

### Python
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        ans = 0

        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
            ans += min(last) + 1

        return ans
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1876. Substrings of Size Three with Distinct Characters](../../1501-2000/1876-substrings-of-size-three-with-distinct-characters/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)
