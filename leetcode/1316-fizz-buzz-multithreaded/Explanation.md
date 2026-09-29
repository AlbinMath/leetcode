# Fizz Buzz Multithreaded

## Problem Explanation
Four threads must cooperate to print the FizzBuzz sequence from `1` to `n`. One thread prints numbers divisible by both 3 and 5 ("fizzbuzz"), one for divisible by 3 only ("fizz"), one for divisible by 5 only ("buzz"), and one for other numbers.

## How the Code Works
The code uses synchronization primitives (mutex + condition variable or semaphores) so that:
1. All four threads run in a loop from `1` to `n`.
2. At each step, only the thread whose condition matches the current number is allowed to proceed and print.
3. After printing, the current number is incremented and all threads are notified to check again.
