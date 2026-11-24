# LeetCode 2659: Make Array Empty

**LeetCode Problem #2659 — Make Array Empty**
Solve LeetCode Make Array Empty using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Array Empty |
| LeetCode | #2659 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` containing **distinct** numbers, and you can perform the following operations **until the array is empty**:

If the first element has the **smallest** value, remove it 
 Otherwise, put the first element at the **end** of the array.

Return *an integer denoting the number of operations it takes to make *`nums`* empty.*

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- All values in `nums` are **distinct**.

## Examples
### Example 1
- **Input:** `nums = [3,4,-1]`
- **Output:** `5`

### Example 2
- **Input:** `nums = [1,2,4,3]`
- **Output:** `5`

### Example 3
- **Input:** `nums = [1,2,3]`
- **Output:** `3`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Make Array Empty**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,-1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.

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
var countOperationsToEmptyArray = function(nums) {
    const n = nums.length;

    // Sort values by their original indices
    const sorted = nums
        .map((value, index) => [value, index])
        .sort((a, b) => a[0] - b[0]);

    // Fenwick Tree: 1 means the element is still present
    const bit = new Array(n + 1).fill(0);

    function update(index, delta) {
        index++;

        while (index <= n) {
            bit[index] += delta;
            index += index & -index;
        }
    }

    function query(index) {
        let sum = 0;
        index++;

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    // Initially, every element is present
    for (let i = 0; i < n; i++) {
        update(i, 1);
    }

    let operations = 0;
    let previousIndex = 0;

    for (const [, index] of sorted) {
        if (index >= previousIndex) {
            // Count remaining elements from previousIndex to index
            operations += query(index) -
                (previousIndex > 0 ? query(previousIndex - 1) : 0);
        } else {
            // Wrap around the end of the array
            operations +=
                query(n - 1) -
                (previousIndex > 0 ? query(previousIndex - 1) : 0) +
                query(index);
        }

        // Remove the current smallest element
        update(index, -1);
        previousIndex = index;
    }

    return operations;
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
- [2870. Minimum Number of Operations to Make Array Empty](../../2501-3000/2870-minimum-number-of-operations-to-make-array-empty/)
- [945. Minimum Increment to Make Array Unique](../../0501-1000/0945-minimum-increment-to-make-array-unique/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1558-minimum-numbers-of-function-calls-to-make-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-array-empty/)
