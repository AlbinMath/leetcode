# LeetCode 1116: Print Zero Even Odd

**LeetCode Problem #1116 — Print Zero Even Odd**
Solve LeetCode Print Zero Even Odd using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print Zero Even Odd |
| LeetCode | #1116 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have a function `printNumber` that can be called with an integer parameter and prints it to the console.

For example, calling `printNumber(7)` prints `7` to the console.

You are given an instance of the class `ZeroEvenOdd` that has three functions: `zero`, `even`, and `odd`. The same instance of `ZeroEvenOdd` will be passed to three different threads:

**Thread A:** calls `zero()` that should only output `0`'s. 
 **Thread B:** calls `even()` that should only output even numbers. 
 **Thread C:** calls `odd()` that should only output odd numbers.

Modify the given class to output the series `"010203040506..."` where the length of the series must be `2n`.

Implement the `ZeroEvenOdd` class:

`ZeroEvenOdd(int n)` Initializes the object with the number `n` that represents the numbers that should be printed. 
 `void zero(printNumber)` Calls `printNumber` to output one zero. 
 `void even(printNumber)` Calls `printNumber` to output one even number. 
 `void odd(printNumber)` Calls `printNumber` to output one odd number.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `"0102"`
- **Explanation:** There are three threads being fired asynchronously.
One of them calls zero(), the other calls even(), and the last one calls odd().
"0102" is the correct output.

### Example 2
- **Input:** `n = 5`
- **Output:** `"0102030405"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
The code uses three **Semaphores** for synchronization.

1. **Semaphore State:** `zero` starts at `1` (goes first), `even` and `odd` start at `0`.
2. **zero thread:** For each number `i` from `1` to `n`, acquires the `zero` semaphore, prints `0`, then releases either `odd` (if `i` is odd) or `even` (if `i` is even).
3. **odd thread:** For each odd number, acquires the `odd` semaphore, prints the odd number, then releases `zero`.
4. **even thread:** For each even number, acquires the `even` semaphore, prints the even number, then releases `zero`.

This creates the pattern: zero→odd→zero→even→zero→odd→... producing `"010203..."`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"0102"`.
4. **Verification:** There are three threads being fired asynchronously.
One of them calls zero(), the other calls even(), and the last one calls odd().
"0102" is the correct output.

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
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.concurrent.Semaphore;
import java.util.function.IntConsumer;

class ZeroEvenOdd {
    private int n;

    private Semaphore zero = new Semaphore(1);
    private Semaphore even = new Semaphore(0);
    private Semaphore odd = new Semaphore(0);

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            zero.acquire();

            printNumber.accept(0);

            if (i % 2 == 1) {
                odd.release();
            } else {
                even.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            even.acquire();

            printNumber.accept(i);

            zero.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            odd.acquire();

            printNumber.accept(i);

            zero.release();
        }
    }
}
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
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)
- [975. Odd Even Jump](../../1001-1500/1017-odd-even-jump/)
- [1609. Even Odd Tree](../../1501-2000/1731-even-odd-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-zero-even-odd/)
