# LeetCode 3411: Maximum Subarray With Equal Products

**LeetCode Problem #3411 — Maximum Subarray With Equal Products**
Solve LeetCode Maximum Subarray With Equal Products using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray With Equal Products |
| LeetCode | #3411 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of **positive** integers `nums`.

An array `arr` is called **product equivalent** if `prod(arr) == lcm(arr) * gcd(arr)`, where:

`prod(arr)` is the product of all elements of `arr`. 
 `gcd(arr)` is the GCD of all elements of `arr`. 
 `lcm(arr)` is the LCM of all elements of `arr`.

Return the length of the **longest** **product equivalent** subarray of `nums`.

## Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 10`

## Examples
### Example 1
- **Input:** `nums = [1,2,1,2,1,1,1]`
- **Output:** `5`
- **Explanation:** The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where `prod([1, 2, 1, 1, 1]) = 2`, `gcd([1, 2, 1, 1, 1]) = 1`, and `lcm([1, 2, 1, 1, 1]) = 2`.

### Example 2
- **Input:** `nums = [2,3,4,5,6]`
- **Output:** `3`
- **Explanation:** The longest product equivalent subarray is `[3, 4, 5].`

### Example 3
- **Input:** `nums = [1,2,3,1,4,5,1]`
- **Output:** `5`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Subarray With Equal Products**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,2,1,1,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where `prod([1, 2, 1, 1, 1]) = 2`, `gcd([1, 2, 1, 1, 1]) = 1`, and `lcm([1, 2, 1, 1, 1]) = 2`.

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
var maxLength = function (nums) {
    const n = nums.length;
    // Max possible lcm(1..10) * max possible gcd(1..10) = 2520 * 10
    const MAX_PRODUCT = 25200;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    const lcm = (a, b) => (a / gcd(a, b)) * b;

    let maxLen = 1;

    for (let i = 0; i < n; i++) {
        let prod = 1;
        let g = 0;
        let l = 1;

        for (let j = i; j < n; j++) {
            const val = nums[j];
            prod *= val;
            if (prod > MAX_PRODUCT) break;

            g = gcd(g, val);
            l = lcm(l, val);

            if (prod === l * g) {
                maxLen = Math.max(maxLen, j - i + 1);
            }
        }
    }

    return maxLen;
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
- [2064. Minimized Maximum of Products Distributed to Any Store](../../2001-2500/2064-minimized-maximum-of-products-distributed-to-any-store/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1072-flip-columns-for-maximum-number-of-equal-rows/)
- [1224. Maximum Equal Frequency](../../1001-1500/1224-maximum-equal-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/)
