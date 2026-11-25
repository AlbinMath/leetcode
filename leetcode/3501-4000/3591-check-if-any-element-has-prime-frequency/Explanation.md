# LeetCode 3591: Check if Any Element Has Prime Frequency

**LeetCode Problem #3591 — Check if Any Element Has Prime Frequency**
Solve LeetCode Check if Any Element Has Prime Frequency using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Any Element Has Prime Frequency |
| LeetCode | #3591 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Return `true` if the frequency of any element of the array is **prime**, otherwise, return `false`.

The **frequency** of an element `x` is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,4]`
- **Output:** `true`
- **Explanation:** 4 has a frequency of two, which is a prime number.

### Example 2
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `false`
- **Explanation:** All elements have a frequency of one.

### Example 3
- **Input:** `nums = [2,2,2,4,4]`
- **Output:** `true`
- **Explanation:** Both 2 and 4 have a prime frequency.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Check if Any Element Has Prime Frequency**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 4 has a frequency of two, which is a prime number.

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
var checkPrimeFrequency = function(nums) {
    const isPrime = (n) => {
        if (n < 2) return false;
        for (let i = 2; i * i <= n; i++) {
            if (n % i === 0) return false;
        }
        return true;
    };

    // 1. Count frequencies (0 <= nums[i] <= 100)
    const freq = new Uint8Array(101);
    for (const num of nums) {
        freq[num]++;
    }

    // 2. Check if any frequency is prime
    for (let i = 0; i <= 100; i++) {
        if (freq[i] > 1 && isPrime(freq[i])) {
            return true;
        }
    }

    return false;
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
- [1784. Check if Binary String Has at Most One Segment of Ones](../../1501-2000/1784-check-if-binary-string-has-at-most-one-segment-of-ones/)
- [2283. Check if Number Has Equal Digit Count and Digit Value](../../2001-2500/2283-check-if-number-has-equal-digit-count-and-digit-value/)
- [2980. Check if Bitwise OR Has Trailing Zeros](../../2501-3000/2980-check-if-bitwise-or-has-trailing-zeros/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-any-element-has-prime-frequency/)
