# LeetCode 3709: Design Exam Scores Tracker

**LeetCode Problem #3709 — Design Exam Scores Tracker**
Solve LeetCode Design Exam Scores Tracker using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Exam Scores Tracker |
| LeetCode | #3709 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Alice frequently takes exams and wants to track her scores and calculate the total scores over specific time periods.

Implement the `ExamTracker` class:

`ExamTracker()`: Initializes the `ExamTracker` object. 
 `void record(int time, int score)`: Alice takes a new exam at time `time` and achieves the score `score`. 
 `long long totalScore(int startTime, int endTime)`: Returns an integer that represents the **total** score of all exams taken by Alice between `startTime` and `endTime` (inclusive). If there are no recorded exams taken by Alice within the specified time interval, return 0.

It is guaranteed that the function calls are made in chronological order. That is,

Calls to `record()` will be made with **strictly increasing** `time`. 
 Alice will never ask for total scores that require information from the future. That is, if the latest `record()` is called with `time = t`, then `totalScore()` will always be called with `startTime <= endTime <= t`.

## Constraints
- `1 <= time <= 10^9`
- `1 <= score <= 10^9`
- `1 <= startTime <= endTime <= t`, where `t` is the value of `time` from the most recent call of `record()`.
- Calls of `record()` will be made with **strictly increasing** `time`.
- After `ExamTracker()`, the first function call will always be `record()`.
- At most `10^5` calls will be made in total to `record()` and `totalScore()`.

## Examples
### Example 1
- **Input:** `["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"] 
[[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]`
- **Output:** `[null, null, 98, null, 98, 197, 0, 99]`
- **Explanation:** ExamTracker examTracker = new ExamTracker(); 
examTracker.record(1, 98); // Alice takes a new exam at time 1, scoring 98. 
examTracker.totalScore(1, 1); // Between time 1 and time 1, Alice took 1 exam at time 1, scoring 98. The total score is 98. 
examTracker.record(5, 99); // Alice takes a new exam at time 5, scoring 99. 
examTracker.totalScore(1, 3); // Between time 1 and time 3, Alice took 1 exam at time 1, scoring 98. The total score is 98. 
examTracker.totalScore(1, 5); // Between time 1 and time 5, Alice took 2 exams at time 1 and 5, scoring 98 and 99. The total score is `98 + 99 = 197`. 
examTracker.totalScore(3, 4); // Alice did not take any exam between time 3 and time 4. Therefore, the answer is 0. 
examTracker.totalScore(2, 5); // Between time 2 and time 5, Alice took 1 exam at time 5, scoring 99. The total score is 99.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Exam Scores Tracker**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"] 
[[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, 98, null, 98, 197, 0, 99]`.
4. **Verification:** ExamTracker examTracker = new ExamTracker(); 
examTracker.record(1, 98); // Alice takes a new exam at time 1, scoring 98. 
examTracker.totalScore(1, 1); // Between time 1 and time 1, Alice took 1 exam at time 1, scoring 98. The total score is 98. 
examTracker.record(5, 99); // Alice takes a new exam at time 5, scoring 99. 
examTracker.totalScore(1, 3); // Between time 1 and time 3, Alice took 1 exam at time 1, scoring 98. The total score is 98. 
examTracker.totalScore(1, 5); // Between time 1 and time 5, Alice took 2 exams at time 1 and 5, scoring 98 and 99. The total score is `98 + 99 = 197`. 
examTracker.totalScore(3, 4); // Alice did not take any exam between time 3 and time 4. Therefore, the answer is 0. 
examTracker.totalScore(2, 5); // Between time 2 and time 5, Alice took 1 exam at time 5, scoring 99. The total score is 99.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var ExamTracker = function() {
    this.times = [];
    this.prefix = [0];
};
ExamTracker.prototype.record = function(time, score) {
    this.times.push(time);
    this.prefix.push(this.prefix[this.prefix.length - 1] + score);
};
ExamTracker.prototype.totalScore = function(startTime, endTime) {
    let lo = 0;
    let hi = this.times.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.times[mid] < startTime) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    const left = lo;
    lo = left;
    hi = this.times.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.times[mid] <= endTime) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    const right = lo;

    return this.prefix[right] - this.prefix[left];
};
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
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0622-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-exam-scores-tracker/)
