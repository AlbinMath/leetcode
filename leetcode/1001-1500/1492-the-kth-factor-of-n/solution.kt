class Solution {
    fun kthFactor(n: Int, k: Int): Int {
        var count = 0
        for (i in 1..n) {
            if (n % i == 0 && ++count == k) return i
        }
        return -1
    }
}
