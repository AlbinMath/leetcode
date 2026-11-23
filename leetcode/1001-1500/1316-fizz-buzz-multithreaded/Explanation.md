# LeetCode 1195: Fizz Buzz Multithreaded

**LeetCode Problem #1195 — Fizz Buzz Multithreaded**
Solve LeetCode Fizz Buzz Multithreaded using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fizz Buzz Multithreaded |
| LeetCode | #1195 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have the four functions:

`printFizz` that prints the word `"fizz"` to the console, 
 `printBuzz` that prints the word `"buzz"` to the console, 
 `printFizzBuzz` that prints the word `"fizzbuzz"` to the console, and 
 `printNumber` that prints a given integer to the console.

You are given an instance of the class `FizzBuzz` that has four functions: `fizz`, `buzz`, `fizzbuzz` and `number`. The same instance of `FizzBuzz` will be passed to four different threads:

**Thread A:** calls `fizz()` that should output the word `"fizz"`. 
 **Thread B:** calls `buzz()` that should output the word `"buzz"`. 
 **Thread C:** calls `fizzbuzz()` that should output the word `"fizzbuzz"`. 
 **Thread D:** calls `number()` that should only output the integers.

Modify the given class to output the series `[1, 2, "fizz", 4, "buzz", ...]` where the `i^th` token (**1-indexed**) of the series is:

`"fizzbuzz"` if `i` is divisible by `3` and `5`, 
 `"fizz"` if `i` is divisible by `3` and not `5`, 
 `"buzz"` if `i` is divisible by `5` and not `3`, or 
 `i` if `i` is not divisible by `3` or `5`.

Implement the `FizzBuzz` class:

`FizzBuzz(int n)` Initializes the object with the number `n` that represents the length of the sequence that should be printed. 
 `void fizz(printFizz)` Calls `printFizz` to output `"fizz"`. 
 `void buzz(printBuzz)` Calls `printBuzz` to output `"buzz"`. 
 `void fizzbuzz(printFizzBuzz)` Calls `printFizzBuzz` to output `"fizzbuzz"`. 
 `void number(printNumber)` Calls `printnumber` to output the numbers.

## Constraints
- `1 <= n <= 50`

## Examples
### Example 1
- **Input:** `n = 15`
- **Output:** `[1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]`

### Example 2
- **Input:** `n = 5`
- **Output:** `[1,2,"fizz",4,"buzz"]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses synchronization primitives (mutex + condition variable or semaphores) so that:
1. All four threads run in a loop from `1` to `n`.
2. At each step, only the thread whose condition matches the current number is allowed to proceed and print.
3. After printing, the current number is incremented and all threads are notified to check again.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 15`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]`.

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
class FizzBuzz {
private:
    int n;
    int current = 1;
    mutex mtx;
    condition_variable cv;

public:
    FizzBuzz(int n) {
        this->n = n;
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        while (true) {
            unique_lock<mutex> lock(mtx);

            cv.wait(lock, [this]() {
                return current > n || (current % 3 == 0 && current % 5 != 0);
            });

            if (current > n)
                return;

            printFizz();
            current++;

            cv.notify_all();
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        while (true) {
            unique_lock<mutex> lock(mtx);

            cv.wait(lock, [this]() {
                return current > n || (current % 5 == 0 && current % 3 != 0);
            });

            if (current > n)
                return;

            printBuzz();
            current++;

            cv.notify_all();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
    void fizzbuzz(function<void()> printFizzBuzz) {
        while (true) {
            unique_lock<mutex> lock(mtx);

            cv.wait(lock, [this]() {
                return current > n || (current % 3 == 0 && current % 5 == 0);
            });

            if (current > n)
                return;

            printFizzBuzz();
            current++;

            cv.notify_all();
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        while (true) {
            unique_lock<mutex> lock(mtx);

            cv.wait(lock, [this]() {
                return current > n ||
                       (current % 3 != 0 && current % 5 != 0);
            });

            if (current > n)
                return;

            printNumber(current);
            current++;

            cv.notify_all();
        }
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
- [412. Fizz Buzz](../../0001-0500/0412-fizz-buzz/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fizz-buzz-multithreaded/)
