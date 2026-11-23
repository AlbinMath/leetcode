# LeetCode 3412: Find Mirror Score of a String

**LeetCode Problem #3412 — Find Mirror Score of a String**
Solve LeetCode Find Mirror Score of a String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Mirror Score of a String |
| LeetCode | #3412 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`.

We define the **mirror** of a letter in the English alphabet as its corresponding letter when the alphabet is reversed. For example, the mirror of `'a'` is `'z'`, and the mirror of `'y'` is `'b'`.

Initially, all characters in the string `s` are **unmarked**.

You start with a score of 0, and you perform the following process on the string `s`:

Iterate through the string from left to right. 
 At each index `i`, find the closest **unmarked** index `j` such that `j < i` and `s[j]` is the mirror of `s[i]`. Then, **mark** both indices `i` and `j`, and add the value `i - j` to the total score. 
 If no such index `j` exists for the index `i`, move on to the next index without making any changes.

Return the total score at the end of the process.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aczzx"`
- **Output:** `5`
- **Explanation:** `i = 0`. There is no index `j` that satisfies the conditions, so we skip. 
 `i = 1`. There is no index `j` that satisfies the conditions, so we skip. 
 `i = 2`. The closest index `j` that satisfies the conditions is `j = 0`, so we mark both indices 0 and 2, and then add `2 - 0 = 2` to the score. 
 `i = 3`. There is no index `j` that satisfies the conditions, so we skip. 
 `i = 4`. The closest index `j` that satisfies the conditions is `j = 1`, so we mark both indices 1 and 4, and then add `4 - 1 = 3` to the score.

### Example 2
- **Input:** `s = "abcdef"`
- **Output:** `0`
- **Explanation:** For each index `i`, there is no index `j` that satisfies the conditions.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Mirror Score of a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aczzx"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** `i = 0`. There is no index `j` that satisfies the conditions, so we skip. 
 `i = 1`. There is no index `j` that satisfies the conditions, so we skip. 
 `i = 2`. The closest index `j` that satisfies the conditions is `j = 0`, so we mark both indices 0 and 2, and then add `2 - 0 = 2` to the score. 
 `i = 3`. There is no index `j` that satisfies the conditions, so we skip. 
 `i = 4`. The closest index `j` that satisfies the conditions is `j = 1`, so we mark both indices 1 and 4, and then add `4 - 1 = 3` to the score.

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
    def calculateScore(self, s: str) -> int:
        score = 0
        unmarked = [[] for _ in range(26)]
        
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            mirror = 25 - c
            
            if unmarked[mirror]:
                j = unmarked[mirror].pop()
                score += i - j
            else:
                unmarked[c].append(i)
                
        return score
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)
- [833. Find And Replace in String](../../0501-1000/0862-find-and-replace-in-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-mirror-score-of-a-string/)
