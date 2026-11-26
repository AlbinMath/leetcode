# LeetCode 821: Shortest Distance to a Character

**LeetCode Problem #821 — Shortest Distance to a Character**
Solve LeetCode Shortest Distance to a Character using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Distance to a Character |
| LeetCode | #821 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` and a character `c` that occurs in `s`, return *an array of integers *`answer`* where *`answer.length == s.length`* and *`answer[i]`* is the **distance** from index *`i`* to the **closest** occurrence of character *`c`* in *`s`.

The **distance** between two indices `i` and `j` is `abs(i - j)`, where `abs` is the absolute value function.

## Constraints
- `1 <= s.length <= 10^4`
- `s[i]` and `c` are lowercase English letters.
- It is guaranteed that `c` occurs at least once in `s`.

## Examples
### Example 1
- **Input:** `s = "loveleetcode", c = "e"`
- **Output:** `[3,2,1,0,1,0,0,1,2,2,1,0]`
- **Explanation:** The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

### Example 2
- **Input:** `s = "aaab", c = "b"`
- **Output:** `[3,2,1,0]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Distance to a Character**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "loveleetcode", c = "e"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,1,0,1,0,0,1,2,2,1,0]`.
4. **Verification:** The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

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
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [float('inf')] * n

        # Left to right: nearest occurrence of c on the left
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # Right to left: nearest occurrence of c on the right
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer
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
- [3243. Shortest Distance After Road Addition Queries I](../../3001-3500/3243-shortest-distance-after-road-addition-queries-i/)
- [3244. Shortest Distance After Road Addition Queries II](../../3001-3500/3244-shortest-distance-after-road-addition-queries-ii/)
- [214. Shortest Palindrome](../../0001-0500/0214-shortest-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-distance-to-a-character/)
