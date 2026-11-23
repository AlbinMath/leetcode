# LeetCode 2671: Frequency Tracker

**LeetCode Problem #2671 — Frequency Tracker**
Solve LeetCode Frequency Tracker using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Frequency Tracker |
| LeetCode | #2671 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

Implement the `FrequencyTracker` class.

`FrequencyTracker()`: Initializes the `FrequencyTracker` object with an empty array initially. 
 `void add(int number)`: Adds `number` to the data structure. 
 `void deleteOne(int number)`: Deletes **one** occurrence of `number` from the data structure. The data structure **may not contain** `number`, and in this case nothing is deleted. 
 `bool hasFrequency(int frequency)`: Returns `true` if there is a number in the data structure that occurs `frequency` number of times, otherwise, it returns `false`.

## Constraints
- `1 <= number <= 10^5`
- `1 <= frequency <= 10^5`
- At most, `2 * 10^5` calls will be made to `add`, `deleteOne`, and `hasFrequency` in **total**.

## Examples
### Example 1
- **Input:** `["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]`
- **Output:** `[null, null, null, true]`
- **Explanation:** FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.add(3); // The data structure now contains [3, 3]
frequencyTracker.hasFrequency(2); // Returns true, because 3 occurs twice

### Example 2
- **Input:** `["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]`
- **Output:** `[null, null, null, false]`
- **Explanation:** FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // The data structure now contains [1]
frequencyTracker.deleteOne(1); // The data structure becomes empty []
frequencyTracker.hasFrequency(1); // Returns false, because the data structure is empty

### Example 3
- **Input:** `["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
[[], [2], [3], [1]]`
- **Output:** `[null, false, null, true]`
- **Explanation:** FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.hasFrequency(2); // Returns false, because the data structure is empty
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.hasFrequency(1); // Returns true, because 3 occurs once

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Frequency Tracker**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, true]`.
4. **Verification:** FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // The data structure now contains [3]
frequencyTracker.add(3); // The data structure now contains [3, 3]
frequencyTracker.hasFrequency(2); // Returns true, because 3 occurs twice

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
var FrequencyTracker = function() {
    this.numFreq = new Map();
    this.freqCount = new Map();
};
FrequencyTracker.prototype.add = function(number) {
    const oldF = this.numFreq.get(number) || 0;
    const newF = oldF + 1;
    
    if (oldF > 0) {
        this.freqCount.set(oldF, this.freqCount.get(oldF) - 1);
    }
    
    this.numFreq.set(number, newF);
    this.freqCount.set(newF, (this.freqCount.get(newF) || 0) + 1);
};
FrequencyTracker.prototype.deleteOne = function(number) {
    const oldF = this.numFreq.get(number) || 0;
    if (oldF === 0) return;
    
    const newF = oldF - 1;
    this.freqCount.set(oldF, this.freqCount.get(oldF) - 1);
    this.numFreq.set(number, newF);
    
    if (newF > 0) {
        this.freqCount.set(newF, (this.freqCount.get(newF) || 0) + 1);
    }
};
FrequencyTracker.prototype.hasFrequency = function(frequency) {
    return (this.freqCount.get(frequency) || 0) > 0;
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
- [2102. Sequentially Ordinal Rank Tracker](../../2001-2500/2207-sequentially-ordinal-rank-tracker/)
- [3709. Design Exam Scores Tracker](../../4001-4500/4059-design-exam-scores-tracker/)
- [192. Word Frequency](../../0001-0500/0192-word-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/frequency-tracker/)
