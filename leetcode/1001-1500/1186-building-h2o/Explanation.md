# LeetCode 1117: Building H2O

**LeetCode Problem #1117 — Building H2O**
Solve LeetCode Building H2O using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Building H2O |
| LeetCode | #1117 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are two kinds of threads: `oxygen` and `hydrogen`. Your goal is to group these threads to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given `releaseHydrogen` and `releaseOxygen` methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads. 
 If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.

We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up with. The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

## Constraints
- `3 * n == water.length`
- `1 <= n <= 20`
- `water[i]` is either `'H'` or `'O'`.
- There will be exactly `2 * n` `'H'` in `water`.
- There will be exactly `n` `'O'` in `water`.

## Examples
### Example 1
- **Input:** `water = "HOH"`
- **Output:** `"HHO"`
- **Explanation:** "HOH" and "OHH" are also valid answers.

### Example 2
- **Input:** `water = "OOHHHH"`
- **Output:** `"HHOHHO"`
- **Explanation:** "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **mutex** and **condition variable** for thread synchronization.

1. **Shared State:** `hydrogenCount` and `oxygenCount` track how many of each have been released in the current molecule.
2. **Hydrogen Thread:**
   - Waits until `hydrogenCount < 2` (room for more hydrogen in the current molecule).
   - Increments `hydrogenCount` and releases the hydrogen.
   - If `hydrogenCount == 2`, notifies all waiting threads (the oxygen thread can now proceed).
3. **Oxygen Thread:**
   - Waits until both hydrogens are ready (`hydrogenCount == 2`) and no oxygen has been released yet (`oxygenCount == 0`).
   - Increments `oxygenCount` and releases the oxygen.
   - Resets both counters to `0` and notifies all threads, allowing the next molecule to start forming.

This ensures every water molecule has exactly 2 H atoms and 1 O atom before any thread proceeds.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `water = "HOH"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"HHO"`.
4. **Verification:** "HOH" and "OHH" are also valid answers.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class H2O {
private:
    mutex mtx;
    condition_variable cv;
    int hydrogenCount = 0;
    int oxygenCount = 0;
public:
    H2O() {
        
    }
    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [&]() {
            return hydrogenCount < 2;
        });
        hydrogenCount++;
        releaseHydrogen();
        if (hydrogenCount == 2) {
            cv.notify_all();
        }
    }
    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [&]() {
            return hydrogenCount == 2 && oxygenCount == 0;
        });
        oxygenCount++;
        releaseOxygen();
        hydrogenCount = 0;
        oxygenCount = 0;
        cv.notify_all();
    }
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
- [1840. Maximum Building Height](../../1501-2000/1968-maximum-building-height/)
- [2940. Find Building Where Alice and Bob Can Meet](../../3001-3500/3181-find-building-where-alice-and-bob-can-meet/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/building-h2o/)
