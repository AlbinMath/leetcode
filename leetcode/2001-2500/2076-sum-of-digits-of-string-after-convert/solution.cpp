
class Solution {
public:
    int getLucky(string s, int k) {
        int sum = 0;

        // Convert each character to its alphabet position
        for (char c : s) {
            int value = c - 'a' + 1;

            // Add the digits of the position
            sum += value / 10;
            sum += value % 10;
        }

        // Perform the remaining digit-sum transformations
        for (int i = 1; i < k; i++) {
            int digitSum = 0;

            while (sum > 0) {
                digitSum += sum % 10;
                sum /= 10;
            }

            sum = digitSum;
        }

        return sum;
    }
};

