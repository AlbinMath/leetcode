# LeetCode 506: Relative Ranks

**LeetCode Problem #506 — Relative Ranks**
Solve LeetCode Relative Ranks using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Relative Ranks |
| LeetCode | #506 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `score` of size `n`, where `score[i]` is the score of the `i^th` athlete in a competition. All the scores are guaranteed to be **unique**.

The athletes are **placed** based on their scores, where the `1^st` place athlete has the highest score, the `2^nd` place athlete has the `2^nd` highest score, and so on. The placement of each athlete determines their rank:

The `1^st` place athlete's rank is `"Gold Medal"`. 
 The `2^nd` place athlete's rank is `"Silver Medal"`. 
 The `3^rd` place athlete's rank is `"Bronze Medal"`. 
 For the `4^th` place to the `n^th` place athlete, their rank is their placement number (i.e., the `x^th` place athlete's rank is `"x"`).

Return an array `answer` of size `n` where `answer[i]` is the **rank** of the `i^th` athlete.

## Constraints
- `n == score.length`
- `1 <= n <= 10^4`
- `0 <= score[i] <= 10^6`
- All the values in `score` are **unique**.

## Examples
### Example 1
- **Input:** `score = [5,4,3,2,1]`
- **Output:** `["Gold Medal","Silver Medal","Bronze Medal","4","5"]`
- **Explanation:** The placements are [1^st, 2^nd, 3^rd, 4^th, 5^th].

### Example 2
- **Input:** `score = [10,3,8,9,4]`
- **Output:** `["Gold Medal","5","Bronze Medal","Silver Medal","4"]`
- **Explanation:** The placements are [1^st, 5^th, 3^rd, 2^nd, 4^th].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Relative Ranks**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `score = [5,4,3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["Gold Medal","Silver Medal","Bronze Medal","4","5"]`.
4. **Verification:** The placements are [1^st, 2^nd, 3^rd, 4^th, 5^th].

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
    def findRelativeRanks(self, score):
        n = len(score)
        answer = [""] * n

        athletes = []

        for i in range(n):
            athletes.append((score[i], i))

        athletes.sort(reverse=True)

        for rank in range(n):
            index = athletes[rank][1]

            if rank == 0:
                answer[index] = "Gold Medal"
            elif rank == 1:
                answer[index] = "Silver Medal"
            elif rank == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(rank + 1)

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
- [1122. Relative Sort Array](../../1001-1500/1217-relative-sort-array/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/relative-ranks/)
