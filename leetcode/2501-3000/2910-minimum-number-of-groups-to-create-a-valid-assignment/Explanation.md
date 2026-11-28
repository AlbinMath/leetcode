# LeetCode 2910: Minimum Number of Groups to Create a Valid Assignment

**LeetCode Problem #2910 — Minimum Number of Groups to Create a Valid Assignment**
Solve LeetCode Minimum Number of Groups to Create a Valid Assignment using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Groups to Create a Valid Assignment |
| LeetCode | #2910 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a collection of numbered `balls` and instructed to sort them into boxes for a nearly balanced distribution. There are two rules you must follow:

Balls with the same box must have the same value. But, if you have more than one ball with the same number, you can put them in different boxes. 
 The biggest box can only have one more ball than the smallest box.

​Return the *fewest number of boxes* to sort these balls following these rules.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `balls = [3,2,3,2,3]`
- **Output:** `2`
- **Explanation:** We can sort `balls` into boxes as follows: 

 
 `[3,3,3]` 
 `[2,2]` 
 

 The size difference between the two boxes doesn't exceed one.

### Example 2
- **Input:** `balls = [10,10,10,3,1,1]`
- **Output:** `4`
- **Explanation:** We can sort `balls` into boxes as follows: 

 
 

 
 `[10]` 
 `[10,10]` 
 `[3]` 
 `[1,1]` 
 

 You can't use fewer than four boxes while still following the rules. For example, putting all three balls numbered 10 in one box would break the rule about the maximum size difference between boxes.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Number of Groups to Create a Valid Assignment**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `balls = [3,2,3,2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can sort `balls` into boxes as follows: 

 
 `[3,3,3]` 
 `[2,2]` 
 

 The size difference between the two boxes doesn't exceed one.

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
var minGroupsForValidAssignment = function(balls) {
    let freq = new Map();
    for (let num of balls) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    let minFreq = Math.min(...freq.values());
    for (let k = minFreq; k >= 1; k--) {
        let ans = 0;
        let valid = true;

        for (let f of freq.values()) {
            let groups = Math.ceil(f / (k + 1));

            if (groups * k > f) {
                valid = false;
                break;
            }

            ans += groups;
        }

        if (valid) {
            return ans;
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
- [3291. Minimum Number of Valid Strings to Form Target I](../../3001-3500/3291-minimum-number-of-valid-strings-to-form-target-i/)
- [3292. Minimum Number of Valid Strings to Form Target II](../../3001-3500/3292-minimum-number-of-valid-strings-to-form-target-ii/)
- [2406. Divide Intervals Into Minimum Number of Groups](../../2001-2500/2406-divide-intervals-into-minimum-number-of-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/)
