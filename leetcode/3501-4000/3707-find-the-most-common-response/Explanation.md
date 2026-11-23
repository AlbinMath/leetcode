# LeetCode 3527: Find the Most Common Response

**LeetCode Problem #3527 — Find the Most Common Response**
Solve LeetCode Find the Most Common Response using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Most Common Response |
| LeetCode | #3527 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D string array `responses` where each `responses[i]` is an array of strings representing survey responses from the `i^th` day.

Return the **most common** response across all days after removing **duplicate** responses within each `responses[i]`. If there is a tie, return the * lexicographically smallest * response.

## Constraints
- `1 <= responses.length <= 1000`
- `1 <= responses[i].length <= 1000`
- `1 <= responses[i][j].length <= 10`
- `responses[i][j]` consists of only lowercase English letters

## Examples
### Example 1
- **Input:** `responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]`
- **Output:** `"good"`
- **Explanation:** After removing duplicates within each list, `responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]`. 
 `"good"` appears 3 times, `"ok"` appears 2 times, and `"bad"` appears 2 times. 
 Return `"good"` because it has the highest frequency.

### Example 2
- **Input:** `responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]`
- **Output:** `"bad"`
- **Explanation:** After removing duplicates within each list we have `responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]`. 
 `"bad"`, `"good"`, and `"ok"` each occur 2 times. 
 The output is `"bad"` because it is the lexicographically smallest amongst the words with the highest frequency.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find the Most Common Response**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"good"`.
4. **Verification:** After removing duplicates within each list, `responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]`. 
 `"good"` appears 3 times, `"ok"` appears 2 times, and `"bad"` appears 2 times. 
 Return `"good"` because it has the highest frequency.

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
var findCommonResponse = function(responses) {
    let freq = new Map();

    // Count each response once per day
    for (const day of responses) {
        let unique = new Set(day);

        for (const word of unique) {
            freq.set(word, (freq.get(word) || 0) + 1);
        }
    }

    let result = "";
    let maxFreq = 0;

    // Find most common response
    for (const [word, count] of freq) {
        if (
            count > maxFreq ||
            (count === maxFreq && word < result)
        ) {
            maxFreq = count;
            result = word;
        }
    }

    return result;
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
- [819. Most Common Word](../../0501-1000/0837-most-common-word/)
- [1002. Find Common Characters](../../1001-1500/1044-find-common-characters/)
- [1979. Find Greatest Common Divisor of Array](../../2001-2500/2106-find-greatest-common-divisor-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-most-common-response/)
