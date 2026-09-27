class Solution {
    fun gcdOfOddEvenSums(n: Int): Int {
        // Sum of first n odd numbers = n²
        val sumOdd = n * n

        // Sum of first n even numbers = n(n + 1)
        val sumEven = n * (n + 1)

        // GCD(n², n(n+1)) = n
        return n
    }
}
