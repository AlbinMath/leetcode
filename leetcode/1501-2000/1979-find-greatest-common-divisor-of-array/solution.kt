class Solution {
    fun findGCD(nums: IntArray): Int {
        var a = nums.minOrNull()!!
        var b = nums.maxOrNull()!!

        while (b != 0) {
            val t = b
            b = a % b
            a = t
        }
        return a
    }
}
