# LeetCode 2899: Last Visited Integers

**LeetCode Problem #2899 — Last Visited Integers**
Solve LeetCode Last Visited Integers using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Last Visited Integers |
| LeetCode | #2899 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` where `nums[i]` is either a positive integer or `-1`. We need to find for each `-1` the respective positive integer, which we call the last visited integer.

To achieve this goal, let's define two empty arrays: `seen` and `ans`.

Start iterating from the beginning of the array `nums`.

If a positive integer is encountered, prepend it to the **front** of `seen`. 
 If `-1` is encountered, let `k` be the number of **consecutive** `-1`s seen so far (including the current `-1`),
 
 If `k` is less than or equal to the length of `seen`, append the `k`-th element of `seen` to `ans`. 
 If `k` is strictly greater than the length of `seen`, append `-1` to `ans`.

Return the array* *`ans`.

## Constraints
- `1 <= nums.length <= 100`
- `nums[i] == -1` or `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,-1,-1,-1]`
- **Output:** `[2,1,-1]`
- **Explanation:** Start with `seen = []` and `ans = []`. 

 
 Process `nums[0]`: The first element in nums is `1`. We prepend it to the front of `seen`. Now, `seen == [1]`. 
 Process `nums[1]`: The next element is `2`. We prepend it to the front of `seen`. Now, `seen == [2, 1]`. 
 Process `nums[2]`: The next element is `-1`. This is the first occurrence of `-1`, so `k == 1`. We look for the first element in seen. We append `2` to `ans`. Now, `ans == [2]`. 
 Process `nums[3]`: Another `-1`. This is the second consecutive `-1`, so `k == 2`. The second element in `seen` is `1`, so we append `1` to `ans`. Now, `ans == [2, 1]`. 
 Process `nums[4]`: Another `-1`, the third in a row, making `k = 3`. However, `seen` only has two elements (`[2, 1]`). Since `k` is greater than the number of elements in `seen`, we append `-1` to `ans`. Finally, `ans == [2, 1, -1]`.

### Example 2
- **Input:** `nums = [1,-1,2,-1,-1]`
- **Output:** `[1,2,1]`
- **Explanation:** Start with `seen = []` and `ans = []`. 

 
 Process `nums[0]`: The first element in nums is `1`. We prepend it to the front of `seen`. Now, `seen == [1]`. 
 Process `nums[1]`: The next element is `-1`. This is the first occurrence of `-1`, so `k == 1`. We look for the first element in `seen`, which is `1`. Append `1` to `ans`. Now, `ans == [1]`. 
 Process `nums[2]`: The next element is `2`. Prepend this to the front of `seen`. Now, `seen == [2, 1]`. 
 Process `nums[3]`: The next element is `-1`. This `-1` is not consecutive to the first `-1` since `2` was in between. Thus, `k` resets to `1`. The first element in `seen` is `2`, so append `2` to `ans`. Now, `ans == [1, 2]`. 
 Process `nums[4]`: Another `-1`. This is consecutive to the previous `-1`, so `k == 2`. The second element in `seen` is `1`, append `1` to `ans`. Finally, `ans == [1, 2, 1]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Last Visited Integers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,-1,-1,-1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,-1]`.
4. **Verification:** Start with `seen = []` and `ans = []`. 

 
 Process `nums[0]`: The first element in nums is `1`. We prepend it to the front of `seen`. Now, `seen == [1]`. 
 Process `nums[1]`: The next element is `2`. We prepend it to the front of `seen`. Now, `seen == [2, 1]`. 
 Process `nums[2]`: The next element is `-1`. This is the first occurrence of `-1`, so `k == 1`. We look for the first element in seen. We append `2` to `ans`. Now, `ans == [2]`. 
 Process `nums[3]`: Another `-1`. This is the second consecutive `-1`, so `k == 2`. The second element in `seen` is `1`, so we append `1` to `ans`. Now, `ans == [2, 1]`. 
 Process `nums[4]`: Another `-1`, the third in a row, making `k = 3`. However, `seen` only has two elements (`[2, 1]`). Since `k` is greater than the number of elements in `seen`, we append `-1` to `ans`. Finally, `ans == [2, 1, -1]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var lastVisitedIntegers = function(nums) {
    const seen = [];
    const ans = [];
    let k = 0;

    for (const num of nums) {
        if (num !== -1) {
            seen.push(num);
            k = 0;
        } else {
            k++;
            if (k <= seen.length) {
                ans.push(seen[seen.length - k]);
            } else {
                ans.push(-1);
            }
        }
    }

    return ans;
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1560. Most Visited Sector in  a Circular Track](../../1501-2000/1682-most-visited-sector-in--a-circular-track/)
- [1581. Customer Who Visited but Did Not Make Any Transactions](../../1501-2000/1724-customer-who-visited-but-did-not-make-any-transactions/)
- [2617. Minimum Number of Visited Cells in a Grid](../../2501-3000/2697-minimum-number-of-visited-cells-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-visited-integers/)
