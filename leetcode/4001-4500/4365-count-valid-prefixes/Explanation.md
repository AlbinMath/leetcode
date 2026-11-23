# LeetCode 4006: Count Valid Prefixes

**LeetCode Problem #4006 — Count Valid Prefixes**
Solve LeetCode Count Valid Prefixes using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Prefixes |
| LeetCode | #4006 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `s`.

A prefix of `s` is considered **valid** if its characters can be rearranged to form an **alternating** string.

Return the number of valid prefixes of `s`.

A string is considered **alternating** if no two adjacent characters are equal.

## Constraints
- `1 <= s.length <= 100`
- `s` consists only of `'0'` and `'1'`.

## Examples
### Example 1
- **Input:** `s = "00101"`
- **Output:** `3`
- **Explanation:** The valid prefixes are: 

 
 `"0"`: It is already an alternating string. 
 `"001"`: It can be rearranged into `"010"`, which is an alternating string. 
 `"00101"`: It can be rearranged into `"01010"`, which is an alternating string. 
 

 Thus, the answer is 3.

### Example 2
- **Input:** `s = "101"`
- **Output:** `3`
- **Explanation:** All prefixes of `s = "101"` are already alternating strings. Thus, the answer is 3.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Valid Prefixes**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "00101"`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The valid prefixes are: 

 
 `"0"`: It is already an alternating string. 
 `"001"`: It can be rearranged into `"010"`, which is an alternating string. 
 `"00101"`: It can be rearranged into `"01010"`, which is an alternating string. 
 

 Thus, the answer is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countValidPrefixes = function(s) {
    let zeros = 0;
    let ones = 0;
    let count = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '0') {
            zeros++;
        } else {
            ones++;
        }

        if (Math.abs(zeros - ones) <= 1) {
            count++;
        }
    }

    return count;
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1461-count-all-valid-pickup-and-delivery-options/)
- [2867. Count Valid Paths in a Tree](../../3001-3500/3112-count-valid-paths-in-a-tree/)
- [3926. Count Valid Word Occurrences](../../4001-4500/4293-count-valid-word-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-prefixes/)
