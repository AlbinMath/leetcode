# LeetCode 2739: Total Distance Traveled

**LeetCode Problem #2739 — Total Distance Traveled**
Solve LeetCode Total Distance Traveled using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Distance Traveled |
| LeetCode | #2739 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A truck has two fuel tanks. You are given two integers, `mainTank` representing the fuel present in the main tank in liters and `additionalTank` representing the fuel present in the additional tank in liters.

The truck has a mileage of `10` km per liter. Whenever `5` liters of fuel get used up in the main tank, if the additional tank has at least `1` liters of fuel, `1` liters of fuel will be transferred from the additional tank to the main tank.

Return *the maximum distance which can be traveled.*

**Note: **Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.

## Constraints
- `1 <= mainTank, additionalTank <= 100`

## Examples
### Example 1
- **Input:** `mainTank = 5, additionalTank = 10`
- **Output:** `60`
- **Explanation:** After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and distance traveled is 50km.
After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty.
Total distance traveled is 60km.

### Example 2
- **Input:** `mainTank = 1, additionalTank = 2`
- **Output:** `10`
- **Explanation:** After spending 1 litre of fuel, the main tank becomes empty.
Total distance traveled is 10km.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Total Distance Traveled**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mainTank = 5, additionalTank = 10`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `60`.
4. **Verification:** After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and distance traveled is 50km.
After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty.
Total distance traveled is 60km.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var distanceTraveled = function(mainTank, additionalTank) {
    const transfers = Math.min(additionalTank, Math.floor((mainTank - 1) / 4));
    return (mainTank + transfers) * 10;
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
- [477. Total Hamming Distance](../../0001-0500/0477-total-hamming-distance/)
- [1741. Find Total Time Spent by Each Employee](../../1501-2000/1892-find-total-time-spent-by-each-employee/)
- [2234. Maximum Total Beauty of the Gardens](../../2001-2500/2330-maximum-total-beauty-of-the-gardens/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-distance-traveled/)
