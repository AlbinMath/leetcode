# LeetCode 1838: Frequency of the Most Frequent Element

**LeetCode Problem #1838 — Frequency of the Most Frequent Element**
Solve LeetCode Frequency of the Most Frequent Element using C++ and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Frequency of the Most Frequent Element |
| LeetCode | #1838 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **frequency** of an element is the number of times it occurs in an array.

You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

Return *the **maximum possible frequency** of an element after performing **at most** *`k`* operations*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,4], k = 5`
- **Output:** `3`
- **Explanation:** Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

### Example 2
- **Input:** `nums = [1,4,8,13], k = 5`
- **Output:** `2`
- **Explanation:** There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

### Example 3
- **Input:** `nums = [3,9,6], k = 2`
- **Output:** `1`

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Frequency of the Most Frequent Element**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,4], k = 5`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int left = 0;
        long long window_sum = 0;
        
        for (int right = 0; right < n; ++right) {
            window_sum += nums[right];
            
            // Preserve the widest valid window seen so far
            if (static_cast<long long>(nums[right]) * (right - left + 1) - window_sum > k) {
                window_sum -= nums[left++];
            }
        }
        
        return n - left;
    }
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [2404. Most Frequent Even Element](../../2001-2500/2404-most-frequent-even-element/)
- [508. Most Frequent Subtree Sum](../../0501-1000/0508-most-frequent-subtree-sum/)
- [2190. Most Frequent Number Following Key In an Array](../../2001-2500/2190-most-frequent-number-following-key-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)
