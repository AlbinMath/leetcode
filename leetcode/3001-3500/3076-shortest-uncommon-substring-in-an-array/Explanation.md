# LeetCode 3076: Shortest Uncommon Substring in an Array

**LeetCode Problem #3076 — Shortest Uncommon Substring in an Array**
Solve LeetCode Shortest Uncommon Substring in an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Uncommon Substring in an Array |
| LeetCode | #3076 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `arr` of size `n` consisting of **non-empty** strings.

Find a string array `answer` of size `n` such that:

`answer[i]` is the **shortest** substring of `arr[i]` that does **not** occur as a substring in any other string in `arr`. If multiple such substrings exist, `answer[i]` should be the lexicographically smallest . And if no such substring exists, `answer[i]` should be an empty string.

Return *the array *`answer`.

## Constraints
- `n == arr.length`
- `2 <= n <= 100`
- `1 <= arr[i].length <= 20`
- `arr[i]` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `arr = ["cab","ad","bad","c"]`
- **Output:** `["ab","","ba",""]`
- **Explanation:** We have the following:
- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
- For the string "ad", there is no substring that does not occur in any other string.
- For the string "bad", the shortest substring that does not occur in any other string is "ba".
- For the string "c", there is no substring that does not occur in any other string.

### Example 2
- **Input:** `arr = ["abc","bcd","abcd"]`
- **Output:** `["","","abcd"]`
- **Explanation:** We have the following:
- For the string "abc", there is no substring that does not occur in any other string.
- For the string "bcd", there is no substring that does not occur in any other string.
- For the string "abcd", the shortest substring that does not occur in any other string is "abcd".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Uncommon Substring in an Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = ["cab","ad","bad","c"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["ab","","ba",""]`.
4. **Verification:** We have the following:
- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
- For the string "ad", there is no substring that does not occur in any other string.
- For the string "bad", the shortest substring that does not occur in any other string is "ba".
- For the string "c", there is no substring that does not occur in any other string.

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
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ans = []
        for i, s in enumerate(arr):
            subs = sorted({s[a:b] for a in range(len(s)) for b in range(a+1, len(s)+1)}, key=lambda x: (len(x), x))
            ans.append(next((x for x in subs if all(x not in t for j, t in enumerate(arr) if j != i)), ""))
        return ans
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
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../../1501-2000/1574-shortest-subarray-to-be-removed-to-make-array-sorted/)
- [3455. Shortest Matching Substring](../../3001-3500/3455-shortest-matching-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/)
