# LeetCode 1865: Finding Pairs With a Certain Sum

**LeetCode Problem #1865 — Finding Pairs With a Certain Sum**
Solve LeetCode Finding Pairs With a Certain Sum using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Finding Pairs With a Certain Sum |
| LeetCode | #1865 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports queries of two types:

**Add** a positive integer to an element of a given index in the array `nums2`. 
 **Count** the number of pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a given value (`0 <= i < nums1.length` and `0 <= j < nums2.length`).

Implement the `FindSumPairs` class:

`FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object with two integer arrays `nums1` and `nums2`. 
 `void add(int index, int val)` Adds `val` to `nums2[index]`, i.e., apply `nums2[index] += val`. 
 `int count(int tot)` Returns the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.

## Constraints
- `1 <= nums1.length <= 1000`
- `1 <= nums2.length <= 10^5`
- `1 <= nums1[i] <= 10^9`
- `1 <= nums2[i] <= 10^5`
- `0 <= index < nums2.length`
- `1 <= val <= 10^5`
- `1 <= tot <= 10^9`
- At most `1000` calls are made to `add` and `count` **each**.

## Examples
### Example 1
- **Input:** `["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]`
- **Output:** `[null, 8, null, 2, 1, null, null, 11]`
- **Explanation:** FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7); // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Finding Pairs With a Certain Sum**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 8, null, 2, 1, null, null, 11]`.
4. **Verification:** FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7); // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,

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
var FindSumPairs = function(nums1, nums2) {
    this.nums1 = nums1;
    this.nums2 = nums2;
    this.freq2 = new Map();
    
    for (const num of nums2) {
        this.freq2.set(num, (this.freq2.get(num) || 0) + 1);
    }
};
FindSumPairs.prototype.add = function(index, val) {
    const oldVal = this.nums2[index];
    this.freq2.set(oldVal, this.freq2.get(oldVal) - 1);
    
    const newVal = oldVal + val;
    this.nums2[index] = newVal;
    this.freq2.set(newVal, (this.freq2.get(newVal) || 0) + 1);
};

FindSumPairs.prototype.count = function(tot) {
    let pairs = 0;
    for (const x of this.nums1) {
        pairs += this.freq2.get(tot - x) || 0;
    }
    return pairs;
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
- [677. Map Sum Pairs](../../0501-1000/0677-map-sum-pairs/)
- [1679. Max Number of K-Sum Pairs](../../1501-2000/1798-max-number-of-k-sum-pairs/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1963-find-xor-sum-of-all-pairs-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/)
