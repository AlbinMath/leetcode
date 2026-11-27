# LeetCode 3712: Sum of Elements With Frequency Divisible by K

**LeetCode Problem #3712 — Sum of Elements With Frequency Divisible by K**
Solve LeetCode Sum of Elements With Frequency Divisible by K using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Elements With Frequency Divisible by K |
| LeetCode | #3712 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Return an integer denoting the **sum** of all elements in `nums` whose ** frequency ** is divisible by `k`, or 0 if there are no such elements.

**Note:** An element is included in the sum **exactly** as many times as it appears in the array if its total frequency is divisible by `k`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,3,3,3,3,4], k = 2`
- **Output:** `16`
- **Explanation:** The number 1 appears once (odd frequency). 
 The number 2 appears twice (even frequency). 
 The number 3 appears four times (even frequency). 
 The number 4 appears once (odd frequency). 
 

 So, the total sum is `2 + 2 + 3 + 3 + 3 + 3 = 16`.

### Example 2
- **Input:** `nums = [1,2,3,4,5], k = 2`
- **Output:** `0`
- **Explanation:** There are no elements that appear an even number of times, so the total sum is 0.

### Example 3
- **Input:** `nums = [4,4,4,1,2,3], k = 3`
- **Output:** `12`
- **Explanation:** The number 1 appears once. 
 The number 2 appears once. 
 The number 3 appears once. 
 The number 4 appears three times. 
 

 So, the total sum is `4 + 4 + 4 = 12`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Sum of Elements With Frequency Divisible by K**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,3,3,3,3,4], k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** The number 1 appears once (odd frequency). 
 The number 2 appears twice (even frequency). 
 The number 3 appears four times (even frequency). 
 The number 4 appears once (odd frequency). 
 

 So, the total sum is `2 + 2 + 3 + 3 + 3 + 3 = 16`.

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
var sumDivisibleByK = function(nums, k) {
    let freq = new Array(101).fill(0);

    // Count frequency
    for (let num of nums) {
        freq[num]++;
    }

    let sum = 0;

    // Check frequency divisible by k
    for (let i = 1; i <= 100; i++) {
        if (freq[i] > 0 && freq[i] % k === 0) {
            sum += i * freq[i];
        }
    }

    return sum;
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
- [2261. K Divisible Elements Subarrays](../../2001-2500/2261-k-divisible-elements-subarrays/)
- [2435. Paths in Matrix Whose Sum Is Divisible by K](../../2001-2500/2435-paths-in-matrix-whose-sum-is-divisible-by-k/)
- [2656. Maximum Sum With Exactly K Elements ](../../2501-3000/2656-maximum-sum-with-exactly-k-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/)
