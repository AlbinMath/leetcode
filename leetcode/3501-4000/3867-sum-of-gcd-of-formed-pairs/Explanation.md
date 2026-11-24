# LeetCode 3867: Sum of GCD of Formed Pairs

**LeetCode Problem #3867 — Sum of GCD of Formed Pairs**
Solve LeetCode Sum of GCD of Formed Pairs using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of GCD of Formed Pairs |
| LeetCode | #3867 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

Construct an array `prefixGcd` where for each index `i`:

Let `mx_i = max(nums[0], nums[1], ..., nums[i])`. 
 `prefixGcd[i] = gcd(nums[i], mx_i)`.

After constructing `prefixGcd`:

Sort `prefixGcd` in **non-decreasing** order. 
 Form pairs by taking the **smallest unpaired** element and the **largest unpaired** element. 
 Repeat this process until no more pairs can be formed. 
 For each formed pair, **compute** the `gcd` of the two elements. 
 If `n` is odd, the **middle** element in the `prefixGcd` array remains **unpaired** and should be ignored.

Return an integer denoting the **sum of the GCD** values of all formed pairs.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^​​​​​​​9`

## Examples
### Example 1
- **Input:** `nums = [2,6,4]`
- **Output:** `2`
- **Explanation:** Construct `prefixGcd`: 

 
 
 
 `i` 
 `nums[i]` 
 `mx_i` 
 `prefixGcd[i]` 
 
 
 
 
 0 
 2 
 2 
 2 
 
 
 1 
 6 
 6 
 6 
 
 
 2 
 4 
 6 
 2 
 
 
 

 `prefixGcd = [2, 6, 2]`. After sorting, it forms `[2, 2, 6]`. 

 Pair the smallest and largest elements: `gcd(2, 6) = 2`. The remaining middle element 2 is ignored. Thus, the sum is 2.

### Example 2
- **Input:** `nums = [3,6,2,8]`
- **Output:** `5`
- **Explanation:** Construct `prefixGcd`: 

 
 
 
 `i` 
 `nums[i]` 
 `mx_i` 
 `prefixGcd[i]` 
 
 
 
 
 0 
 3 
 3 
 3 
 
 
 1 
 6 
 6 
 6 
 
 
 2 
 2 
 6 
 2 
 
 
 3 
 8 
 8 
 8 
 
 
 

 `prefixGcd = [3, 6, 2, 8]`. After sorting, it forms `[2, 3, 6, 8]`. 

 Form pairs: `gcd(2, 8) = 2` and `gcd(3, 6) = 3`. Thus, the sum is `2 + 3 = 5`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sum of GCD of Formed Pairs**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,6,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Construct `prefixGcd`: 

 
 
 
 `i` 
 `nums[i]` 
 `mx_i` 
 `prefixGcd[i]` 
 
 
 
 
 0 
 2 
 2 
 2 
 
 
 1 
 6 
 6 
 6 
 
 
 2 
 4 
 6 
 2 
 
 
 

 `prefixGcd = [2, 6, 2]`. After sorting, it forms `[2, 2, 6]`. 

 Pair the smallest and largest elements: `gcd(2, 6) = 2`. The remaining middle element 2 is ignored. Thus, the sum is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        vector<int> prefixGcd;
        int mx = 0;

        // Construct prefixGcd
        for (int x : nums) {
            mx = max(mx, x);
            prefixGcd.push_back(gcd(x, mx));
        }

        // Sort prefixGcd
        sort(prefixGcd.begin(), prefixGcd.end());

        // Pair smallest with largest
        long long ans = 0;
        int left = 0;
        int right = prefixGcd.size() - 1;

        while (left < right) {
            ans += gcd(prefixGcd[left], prefixGcd[right]);
            left++;
            right--;
        }

        return ans;
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [677. Map Sum Pairs](../../0501-1000/0677-map-sum-pairs/)
- [1679. Max Number of K-Sum Pairs](../../1501-2000/1679-max-number-of-k-sum-pairs/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1835-find-xor-sum-of-all-pairs-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/)
