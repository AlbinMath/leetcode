# LeetCode 1209: Remove All Adjacent Duplicates in String II

**LeetCode Problem #1209 — Remove All Adjacent Duplicates in String II**
Solve LeetCode Remove All Adjacent Duplicates in String II using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove All Adjacent Duplicates in String II |
| LeetCode | #1209 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` and an integer `k`, a `k` **duplicate removal** consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `k` **duplicate removals** on `s` until we no longer can.

Return *the final string after all such duplicate removals have been made*. It is guaranteed that the answer is **unique**.

## Constraints
- `1 <= s.length <= 10^5`
- `2 <= k <= 10^4`
- `s` only contains lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcd", k = 2`
- **Output:** `"abcd"`
- **Explanation:** There's nothing to delete.

### Example 2
- **Input:** `s = "deeedbbcccbdaa", k = 3`
- **Output:** `"aa"`
- **Explanation:** First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

### Example 3
- **Input:** `s = "pbbcggttciiippooaais", k = 2`
- **Output:** `"ps"`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove All Adjacent Duplicates in String II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcd", k = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abcd"`.
4. **Verification:** There's nothing to delete.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])

            if stack[-1][1] == k:
                stack.pop()

        return ''.join(ch * count for ch, count in stack)
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1047. Remove All Adjacent Duplicates In String](../../1001-1500/1128-remove-all-adjacent-duplicates-in-string/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../../0001-0500/0080-remove-duplicates-from-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)
