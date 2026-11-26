# LeetCode 2019: The Score of Students Solving Math Expression

**LeetCode Problem #2019 — The Score of Students Solving Math Expression**
Solve LeetCode The Score of Students Solving Math Expression using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Score of Students Solving Math Expression |
| LeetCode | #2019 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` that contains digits `0-9`, addition symbols `'+'`, and multiplication symbols `'*'` **only**, representing a **valid** math expression of **single digit numbers** (e.g., `3+5*2`). This expression was given to `n` elementary school students. The students were instructed to get the answer of the expression by following this **order of operations**:

Compute **multiplication**, reading from **left to right**; Then, 
 Compute **addition**, reading from **left to right**.

You are given an integer array `answers` of length `n`, which are the submitted answers of the students in no particular order. You are asked to grade the `answers`, by following these **rules**:

If an answer **equals** the correct answer of the expression, this student will be rewarded `5` points; 
 Otherwise, if the answer **could be interpreted** as if the student applied the operators **in the wrong order** but had **correct arithmetic**, this student will be rewarded `2` points; 
 Otherwise, this student will be rewarded `0` points.

Return *the sum of the points of the students*.

## Constraints
- `3 <= s.length <= 31`
- `s` represents a valid expression that contains only digits `0-9`, `'+'`, and `'*'` only.
- All the integer operands in the expression are in the **inclusive** range `[0, 9]`.
- `1 <=` The count of all operators (`'+'` and `'*'`) in the math expression `<= 15`
- Test data are generated such that the correct answer of the expression is in the range of `[0, 1000]`.
- Test data are generated such that value never exceeds 10^9 in intermediate steps of multiplication.
- `n == answers.length`
- `1 <= n <= 10^4`
- `0 <= answers[i] <= 1000`

## Examples
### Example 1
- **Input:** `s = "7+3*1*2", answers = [20,13,42]`
- **Output:** `7`
- **Explanation:** As illustrated above, the correct answer of the expression is 13, therefore one student is rewarded 5 points: [20,

### Example 2
- **Input:** `s = "3+5*2", answers = [13,0,10,13,13,16,16]`
- **Output:** `19`
- **Explanation:** The correct answer of the expression is 13, therefore three students are rewarded 5 points each: [

### Example 3
- **Input:** `s = "6+0*1", answers = [12,9,6,4,8,6]`
- **Output:** `10`
- **Explanation:** The correct answer of the expression is 6.
If a student had incorrectly done (6+0)*1, the answer would also be 6.
By the rules of grading, the students will still be rewarded 5 points (as they got the correct answer), not 2 points.
The points for the students are: [0,0,5,0,0,5]. The sum of the points is 10.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **The Score of Students Solving Math Expression**, we observe the problem requirements and utilize the **Math & Logic** technique. By maintaining a **Primitive Types**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Primitive Types** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "7+3*1*2", answers = [20,13,42]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** As illustrated above, the correct answer of the expression is 13, therefore one student is rewarded 5 points: [20,

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
from typing import List
from collections import Counter

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        d = [int(c) for c in s[0::2]]
        op = s[1::2]
        m = len(d)
        LIM = 1000

        # correct value
        total = 0
        term = d[0]
        for i in range(m - 1):
            if op[i] == '*':
                term *= d[i + 1]
            else:
                total += term
                term = d[i + 1]
        total += term
        correct = total

        # S[i][j]: values <= LIM obtainable from d[i..j]
        # Z[i][j]: True if the interval can evaluate to 0 even through an
        #          over-limit value (so a product with a zero side gives 0)
        S = [[set() for _ in range(m)] for _ in range(m)]
        for i in range(m):
            S[i][i].add(d[i])
        for length in range(2, m + 1):
            for i in range(m - length + 1):
                j = i + length - 1
                cur = S[i][j]
                for k in range(i, j):
                    L, R = S[i][k], S[k + 1][j]
                    if op[k] == '+':
                        for a in L:
                            for b in R:
                                v = a + b
                                if v <= LIM:
                                    cur.add(v)
                    else:
                        for a in L:
                            for b in R:
                                v = a * b
                                if v <= LIM:
                                    cur.add(v)
                        # an over-limit side times a zero side gives 0
                        if 0 in L or 0 in R:
                            cur.add(0)

        possible = S[0][m - 1]
        cnt = Counter(answers)
        score = 0
        for v, c in cnt.items():
            if v == correct:
                score += 5 * c
            elif v in possible:
                score += 2 * c
        return score
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
- [2545. Sort the Students by Their Kth Score](../../2501-3000/2545-sort-the-students-by-their-kth-score/)
- [798. Smallest Rotation with Highest Score](../../0501-1000/0798-smallest-rotation-with-highest-score/)
- [856. Score of Parentheses](../../0501-1000/0856-score-of-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-score-of-students-solving-math-expression/)
