object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        var first = 0
        var second = 0

        for (num <- nums) {
            if (num > first) {
                second = first
                first = num
            } else if (num > second) {
                second = num
            }
        }

        (first - 1) * (second - 1)
    }
}

