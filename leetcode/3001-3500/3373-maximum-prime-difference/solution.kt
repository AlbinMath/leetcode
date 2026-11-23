class Solution {
    fun maximumPrimeDifference(nums: IntArray): Int {
        var first = -1
        var last = -1
        for (i in nums.indices) {
            val x = nums[i]
            var prime = x >= 2
            for (d in 2..kotlin.math.sqrt(x.toDouble()).toInt()) {
                if (x % d == 0) {
                    prime = false
                    break
                }
            }
            if (prime) {
                if (first == -1) first = i
                last = i
            }
        }
        return last - first
    }
}
