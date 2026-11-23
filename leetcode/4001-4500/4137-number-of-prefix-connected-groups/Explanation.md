# LeetCode 3839: Number of Prefix Connected Groups

**LeetCode Problem #3839 — Number of Prefix Connected Groups**
Solve LeetCode Number of Prefix Connected Groups using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Prefix Connected Groups |
| LeetCode | #3839 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of strings `words` and an integer `k`.

Two words `a` and `b` at **distinct indices** are ** prefix -connected** if `a[0..k-1] == b[0..k-1]`.

A **connected group** is a set of words such that each pair of words is prefix-connected.

Return the **number of connected groups** that contain **at least** two words, formed from the given words.

**Note:**

Words with length less than `k` cannot join any group and are ignored. 
 Duplicate strings are treated as separate words.

## Constraints
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 100`
- `1 <= k <= 100`
- All strings in `words` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["apple","apply","banana","bandit"], k = 2`
- **Output:** `2`
- **Explanation:** Words sharing the same first `k = 2` letters are grouped together: 

 
 `words[0] = "apple"` and `words[1] = "apply"` share prefix `"ap"`. 
 `words[2] = "banana"` and `words[3] = "bandit"` share prefix `"ba"`. 
 

 Thus, there are 2 connected groups, each containing at least two words.

### Example 2
- **Input:** `words = ["car","cat","cartoon"], k = 3`
- **Output:** `1`
- **Explanation:** Words are evaluated for a prefix of length `k = 3`: 

 
 `words[0] = "car"` and `words[2] = "cartoon"` share prefix `"car"`. 
 `words[1] = "cat"` does not share a 3-length prefix with any other word. 
 

 Thus, there is 1 connected group.

### Example 3
- **Input:** `words = ["bat","dog","dog","doggy","bat"] , k = 3`
- **Output:** `2`
- **Explanation:** Words are evaluated for a prefix of length `k = 3`: 

 
 `words[0] = "bat"` and `words[4] = "bat"` form a group. 
 `words[1] = "dog"`, `words[2] = "dog"` and `words[3] = "doggy"` share prefix `"dog"`. 
 

 Thus, there are 2 connected groups, each containing at least two words.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Prefix Connected Groups**, we observe the problem requirements and utilize the **Prefix Sum** technique. By maintaining a **Prefix Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Prefix Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["apple","apply","banana","bandit"], k = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Words sharing the same first `k = 2` letters are grouped together: 

 
 `words[0] = "apple"` and `words[1] = "apply"` share prefix `"ap"`. 
 `words[2] = "banana"` and `words[3] = "bandit"` share prefix `"ba"`. 
 

 Thus, there are 2 connected groups, each containing at least two words.

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
var prefixConnected = function(words, k) {
    const map = new Map();

    // Step 1: Count prefix frequencies
    for (let word of words) {
        if (word.length < k) {
            continue;
        }

        const prefix = word.substring(0, k);

        map.set(prefix, (map.get(prefix) || 0) + 1);
    }

    // Step 2: Count groups with at least 2 words
    let count = 0;

    for (let freq of map.values()) {
        if (freq >= 2) {
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
- [1319. Number of Operations to Make Network Connected](../../1001-1500/1442-number-of-operations-to-make-network-connected/)
- [1815. Maximum Number of Groups Getting Fresh Donuts](../../1501-2000/1924-maximum-number-of-groups-getting-fresh-donuts/)
- [2493. Divide Nodes Into the Maximum Number of Groups](../../2501-3000/2583-divide-nodes-into-the-maximum-number-of-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-prefix-connected-groups/)
