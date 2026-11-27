# LeetCode 2512: Reward Top K Students

**LeetCode Problem #2512 — Reward Top K Students**
Solve LeetCode Reward Top K Students using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reward Top K Students |
| LeetCode | #2512 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two string arrays `positive_feedback` and `negative_feedback`, containing the words denoting positive and negative feedback, respectively. Note that **no** word is both positive and negative.

Initially every student has `0` points. Each positive word in a feedback report **increases** the points of a student by `3`, whereas each negative word **decreases** the points by `1`.

You are given `n` feedback reports, represented by a **0-indexed** string array `report` and a **0-indexed** integer array `student_id`, where `student_id[i]` represents the ID of the student who has received the feedback report `report[i]`. The ID of each student is **unique**.

Given an integer `k`, return *the top *`k`* students after ranking them in **non-increasing** order by their points*. In case more than one student has the same points, the one with the lower ID ranks higher.

## Constraints
- `1 <= positive_feedback.length, negative_feedback.length <= 10^4`
- `1 <= positive_feedback[i].length, negative_feedback[j].length <= 100`
- Both `positive_feedback[i]` and `negative_feedback[j]` consists of lowercase English letters.
- No word is present in both `positive_feedback` and `negative_feedback`.
- `n == report.length == student_id.length`
- `1 <= n <= 10^4`
- `report[i]` consists of lowercase English letters and spaces `' '`.
- There is a single space between consecutive words of `report[i]`.
- `1 <= report[i].length <= 100`
- `1 <= student_id[i] <= 10^9`
- All the values of `student_id[i]` are **unique**.
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2`
- **Output:** `[1,2]`
- **Explanation:** Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.

### Example 2
- **Input:** `positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2`
- **Output:** `[2,1]`
- **Explanation:** - The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points. 
- The student with ID 2 has 1 positive feedback, so he has 3 points. 
Since student 2 has more points, [2,1] is returned.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reward Top K Students**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var topStudents = function(positive_feedback, negative_feedback, report, student_id, k) {
    const positive = new Set(positive_feedback);
    const negative = new Set(negative_feedback);

    const students = [];

    for (let i = 0; i < report.length; i++) {
        const words = report[i].split(" ");

        let score = 0;

        for (const word of words) {
            if (positive.has(word)) {
                score += 3;
            } else if (negative.has(word)) {
                score -= 1;
            }
        }

        students.push({
            id: student_id[i],
            score: score
        });
    }

    students.sort((a, b) => {
        if (a.score !== b.score) {
            return b.score - a.score;
        }

        return a.id - b.id;
    });

    return students.slice(0, k).map(student => student.id);
};
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
- [347. Top K Frequent Elements](../../0001-0500/0347-top-k-frequent-elements/)
- [692. Top K Frequent Words](../../0501-1000/0692-top-k-frequent-words/)
- [3070. Count Submatrices with Top-Left Element and Sum Less Than k](../../3001-3500/3070-count-submatrices-with-top-left-element-and-sum-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reward-top-k-students/)
