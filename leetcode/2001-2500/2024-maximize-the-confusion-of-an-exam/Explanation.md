# LeetCode 2024: Maximize the Confusion of an Exam

**LeetCode Problem #2024 — Maximize the Confusion of an Exam**
Solve LeetCode Maximize the Confusion of an Exam using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Confusion of an Exam |
| LeetCode | #2024 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A teacher is writing a test with `n` true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by **maximizing** the number of **consecutive** questions with the **same** answer (multiple trues or multiple falses in a row).

You are given a string `answerKey`, where `answerKey[i]` is the original answer to the `i^th` question. In addition, you are given an integer `k`, the maximum number of times you may perform the following operation:

Change the answer key for any question to `'T'` or `'F'` (i.e., set `answerKey[i]` to `'T'` or `'F'`).

Return *the **maximum** number of consecutive* `'T'`s or `'F'`s *in the answer key after performing the operation at most* `k` *times*.

## Constraints
- `n == answerKey.length`
- `1 <= n <= 5 * 10^4`
- `answerKey[i]` is either `'T'` or `'F'`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `answerKey = "TTFF", k = 2`
- **Output:** `4`
- **Explanation:** We can replace both the 'F's with 'T's to make answerKey = " TTTT ".
There are four consecutive 'T's.

### Example 2
- **Input:** `answerKey = "TFFT", k = 1`
- **Output:** `3`
- **Explanation:** We can replace the first 'T' with an 'F' to make answerKey = " FFF T".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "T FFF ".
In both cases, there are three consecutive 'F's.

### Example 3
- **Input:** `answerKey = "TTFTTFTT", k = 1`
- **Output:** `5`
- **Explanation:** We can replace the first 'F' to make answerKey = " TTTTT FTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTF TTTTT ". 
In both cases, there are five consecutive 'T's.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize the Confusion of an Exam**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `answerKey = "TTFF", k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can replace both the 'F's with 'T's to make answerKey = " TTTT ".
There are four consecutive 'T's.

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
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_T = count_F = max_freq = left = 0
        
        for right, ch in enumerate(answerKey):
            if ch == 'T':
                count_T += 1
                if count_T > max_freq:
                    max_freq = count_T
            else:
                count_F += 1
                if count_F > max_freq:
                    max_freq = count_F
                    
            if (right - left + 1) - max_freq > k:
                if answerKey[left] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1
                left += 1
                
        return len(answerKey) - left
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
- [855. Exam Room](../../0501-1000/0855-exam-room/)
- [1349. Maximum Students Taking Exam](../../1001-1500/1349-maximum-students-taking-exam/)
- [3709. Design Exam Scores Tracker](../../3501-4000/3709-design-exam-scores-tracker/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/)
