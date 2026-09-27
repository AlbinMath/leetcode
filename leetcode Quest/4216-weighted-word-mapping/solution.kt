class Solution {
    fun mapWordWeights(words: Array<String>, weights: IntArray): String {
        val result = StringBuilder()

        for (word in words) {
            var sum = 0

            for (c in word) {
                sum += weights[c - 'a']
            }

            val index = sum % 26

            // Reverse alphabetical order:
            // 0 -> z, 1 -> y, ..., 25 -> a
            result.append(('z'.code - index).toChar())
        }

        return result.toString()
    }
}
