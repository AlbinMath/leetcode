# LeetCode 3921: Score Validator

**LeetCode Problem #3921 — Score Validator**
Solve LeetCode Score Validator using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Score Validator |
| LeetCode | #3921 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string array `events`.

Initially, `score = 0` and `counter = 0`. Each element in `events` is one of the following:

`"0"`, `"1"`, `"2"`, `"3"`, `"4"`, `"6"`: Add that value to the total score. 
 `"W"`: Increase the counter by 1. No score is added. 
 `"WD"`: Add 1 to the total score. 
 `"NB"`: Add 1 to the total score.

Process the array from left to right. Stop processing when either:

All elements in `events` have been processed, or 
 The counter becomes 10.

Return an integer array `[score, counter]`, where:

`score` is the final total score. 
 `counter` is the final counter value.

## Constraints
- `1 <= events.length <= 1000`
- `events[i]` is one of `"0"`, `"1"`, `"2"`, `"3"`, `"4"`, `"6"`, `"W"`, `"WD"`, or `"NB"`.

## Examples
### Example 1
- **Input:** `events = ["1","4","W","6","WD"]`
- **Output:** `[12,1]`
- **Explanation:** Event 
 Score 
 Counter 
 
 
 `"1"` 
 1 
 0 
 
 
 `"4"` 
 5 
 0 
 
 
 `"W"` 
 5 
 1 
 
 
 `"6"` 
 11 
 1 
 
 
 `"WD"` 
 12 
 1 
 
 
 

 Final result: `[12, 1]`.

### Example 2
- **Input:** `events = ["WD","NB","0","4","4"]`
- **Output:** `[10,0]`
- **Explanation:** Event 
 Score 
 Counter 
 
 
 `"WD"` 
 1 
 0 
 
 
 `"NB"` 
 2 
 0 
 
 
 `"0"` 
 2 
 0 
 
 
 `"4"` 
 6 
 0 
 
 
 `"4"` 
 10 
 0 
 
 
 

 Final result: `[10, 0]`.

### Example 3
- **Input:** `events = ["W","W","W","W","W","W","W","W","W","W","W"]`
- **Output:** `[0,10]`
- **Explanation:** After 10 occurrences of `"W"`, the counter reaches 10, so processing stops. The remaining events are ignored.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Score Validator**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `events = ["1","4","W","6","WD"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[12,1]`.
4. **Verification:** Event 
 Score 
 Counter 
 
 
 `"1"` 
 1 
 0 
 
 
 `"4"` 
 5 
 0 
 
 
 `"W"` 
 5 
 1 
 
 
 `"6"` 
 11 
 1 
 
 
 `"WD"` 
 12 
 1 
 
 
 

 Final result: `[12, 1]`.

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
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = counter = 0
        for e in events:
            if e == "W":
                counter += 1
                if counter == 10:
                    break
            elif e == "WD" or e == "NB":
                score += 1
            else:
                score += int(e)
        return [score, counter]
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
- [856. Score of Parentheses](../../0501-1000/0886-score-of-parentheses/)
- [861. Score After Flipping Matrix](../../0501-1000/0891-score-after-flipping-matrix/)
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1381-maximum-score-words-formed-by-letters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/score-validator/)
