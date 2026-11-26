# LeetCode 628: Maximum Product of Three Numbers

**LeetCode Problem #628 — Maximum Product of Three Numbers**
Solve LeetCode Maximum Product of Three Numbers using Elixir and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Three Numbers |
| LeetCode | #628 |
| Difficulty | Easy |
| Language | Elixir |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Find three numbers whose product is **maximum** and return the **maximum** product.

## Constraints
- `3 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,-3]`
- **Output:** `-6`
- **Explanation:** The only three numbers are 1, 2, and -3, so the maximum product is `1 * 2 * -3 = -6`.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `24`
- **Explanation:** The largest product comes from the three greatest numbers: `2 * 3 * 4 = 24`.

### Example 3
- **Input:** `nums = [-1,-2,-3]`
- **Output:** `-6`
- **Explanation:** The only three numbers are -1, -2, and -3, so the maximum product is `(-1) * (-2) * (-3) = -6`.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **sorting** and considers two possible candidates for the maximum product:

1. **Sort the Array:** Sort `nums` in ascending order.
2. **Two Candidates:**
   - `a * b * c` — the product of the three largest numbers (last three elements in the sorted array).
   - `a * x * y` — the product of the largest number and the two smallest numbers (first two elements). This handles the case where two large negative numbers multiply to give a large positive result.
3. Return the maximum of these two candidates.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,-3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `-6`.
4. **Verification:** The only three numbers are 1, 2, and -3, so the maximum product is `1 * 2 * -3 = -6`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Elixir

## Source Code
- [solution.ex](./solution.ex)


```elixir
defmodule Solution do

  @spec maximum_product(nums :: [integer]) :: integer

  def maximum_product(nums) do
    sorted = Enum.sort(nums)

    n = length(sorted)

    a = Enum.at(sorted, n - 1)
    b = Enum.at(sorted, n - 2)
    c = Enum.at(sorted, n - 3)

    x = Enum.at(sorted, 0)
    y = Enum.at(sorted, 1)

    max(a * b * c, a * x * y)
  end

end
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1352. Product of the Last K Numbers](../../1001-1500/1352-product-of-the-last-k-numbers/)
- [3256. Maximum Value Sum by Placing Three Rooks I](../../3001-3500/3256-maximum-value-sum-by-placing-three-rooks-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/)
