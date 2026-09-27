class Solution {
    fun sumAndMultiply(n: Int): Long {
        var num = n
        var x = 0L
        var sum = 0L
        var place = 1L

        while (num > 0) {
            val digit = num % 10

            if (digit != 0) {
                x += digit * place
                sum += digit
                place *= 10
            }

            num /= 10
        }

        return x * sum
    }
}
