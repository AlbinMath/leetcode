class Solution {
    fun leftRightDifference(nums: IntArray): IntArray {
        val n = nums.size
        val answer = IntArray(n)

        var total = nums.sum()
        var leftSum = 0

        for (i in 0 until n) {
            // Remove current element from total
            total -= nums[i]

            // total is now the right sum
            answer[i] = kotlin.math.abs(leftSum - total)

            // Add current element to left sum
            leftSum += nums[i]
        }

        return answer
    }
}
