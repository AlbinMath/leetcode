class Solution {
    fun findGCD(nums: IntArray): Int {
        var min = nums.minOrNull()!!
        var max = nums.maxOrNull()!!

        while (max != 0) {
            val temp = max
            max = min % max
            min = temp
        }

        return min
    }
}
