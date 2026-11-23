# LeetCode 1837: Sum of Digits in Base K

**LeetCode Problem #1837 — Sum of Digits in Base K**
Solve LeetCode Sum of Digits in Base K using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Digits in Base K |
| LeetCode | #1837 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n` (in base `10`) and a base `k`, return *the **sum** of the digits of *`n`* **after** converting *`n`* from base *`10`* to base *`k`.

After converting, each digit should be interpreted as a base `10` number, and the sum should be returned in base `10`.

## Constraints
- `1 <= n <= 100`
- `2 <= k <= 10`

## Examples
### Example 1
- **Input:** `n = 34, k = 6`
- **Output:** `9`
- **Explanation:** 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

### Example 2
- **Input:** `n = 10, k = 10`
- **Output:** `1`
- **Explanation:** n is already in base 10. 1 + 0 = 1.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Digits in Base K**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 34, k = 6`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int sumBase(int n, int k) {
        int sum = 0;

        while (n > 0) {
            sum += n % k;
            n /= k;
        }

        return sum;
    }
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)
- [560. Subarray Sum Equals K](../../0501-1000/0560-subarray-sum-equals-k/)
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-digits-in-base-k/)
