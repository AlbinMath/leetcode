class Solution {
    fun largestInteger(nums: IntArray, k: Int): Int {
        val count = HashMap<Int, Int>()
        val n = nums.size

        for (i in 0..n - k) {
            val seen = HashSet<Int>()

            for (j in i until i + k) {
                seen.add(nums[j])
            }

            for (x in seen) {
                count[x] = (count[x] ?: 0) + 1
            }
        }

        var ans = -1

        for ((x, freq) in count) {
            if (freq == 1) {
                ans = maxOf(ans, x)
            }
        }

        return ans
    }
}
