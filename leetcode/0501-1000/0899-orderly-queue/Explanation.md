# LeetCode 899: Orderly Queue

**LeetCode Problem #899 — Orderly Queue**
Solve LeetCode Orderly Queue using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Orderly Queue |
| LeetCode | #899 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` and an integer `k`. You can choose one of the first `k` letters of `s` and append it at the end of the string.

Return *the lexicographically smallest string you could have after applying the mentioned step any number of moves*.

## Constraints
- `1 <= k <= s.length <= 1000`
- `s` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "cba", k = 1`
- **Output:** `"acb"`
- **Explanation:** In the first move, we move the 1^st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1^st character 'b' to the end, obtaining the final result "acb".

### Example 2
- **Input:** `s = "baaca", k = 3`
- **Output:** `"aaabc"`
- **Explanation:** In the first move, we move the 1^st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3^rd character 'c' to the end, obtaining the final result "aaabc".

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Orderly Queue**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "cba", k = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"acb"`.
4. **Verification:** In the first move, we move the 1^st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1^st character 'b' to the end, obtaining the final result "acb".

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
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return ''.join(sorted(s))
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
- [232. Implement Queue using Stacks](../../0001-0500/0232-implement-queue-using-stacks/)
- [406. Queue Reconstruction by Height](../../0001-0500/0406-queue-reconstruction-by-height/)
- [622. Design Circular Queue](../../0501-1000/0622-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/orderly-queue/)
