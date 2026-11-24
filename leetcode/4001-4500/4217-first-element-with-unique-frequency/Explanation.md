# LeetCode 3843: First Element with Unique Frequency

**LeetCode Problem #3843 — First Element with Unique Frequency**
Solve LeetCode First Element with Unique Frequency using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Element with Unique Frequency |
| LeetCode | #3843 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Return an integer denoting the **first** element (scanning from left to right) in `nums` whose **frequency** is **unique**. That is, no other integer appears the same number of times in `nums`. If there is no such element, return -1.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [20,10,30,30]`
- **Output:** `30`
- **Explanation:** 20 appears once. 
 10 appears once. 
 30 appears twice. 
 The frequency of 30 is unique because no other integer appears exactly twice.

### Example 2
- **Input:** `nums = [20,20,10,30,30,30]`
- **Output:** `20`
- **Explanation:** 20 appears twice. 
 10 appears once. 
 30 appears 3 times. 
 The frequency of 20, 10, and 30 are unique. The first element that has unique frequency is 20.

### Example 3
- **Input:** `nums = [10,10,20,20]`
- **Output:** `-1`
- **Explanation:** 10 appears twice. 
 20 appears twice. 
 No element has a unique frequency.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **First Element with Unique Frequency**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [20,10,30,30]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `30`.
4. **Verification:** 20 appears once. 
 10 appears once. 
 30 appears twice. 
 The frequency of 30 is unique because no other integer appears exactly twice.

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
var firstUniqueFreq = function(nums) {
    const freq = new Map();

    // Step 1: Count frequency of each number
    for (let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Step 2: Count how many numbers have each frequency
    const freqCount = new Map();

    for (let count of freq.values()) {
        freqCount.set(count, (freqCount.get(count) || 0) + 1);
    }

    // Step 3: Find the first number with unique frequency
    for (let num of nums) {
        const count = freq.get(num);

        if (freqCount.get(count) === 1) {
            return num;
        }
    }

    return -1;
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
- [3866. First Unique Even Element](../../4001-4500/4252-first-unique-even-element/)
- [1838. Frequency of the Most Frequent Element](../../1501-2000/1966-frequency-of-the-most-frequent-element/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3501-4000/3622-maximum-frequency-of-an-element-after-performing-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-element-with-unique-frequency/)
