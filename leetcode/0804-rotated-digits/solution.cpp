class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;

        for (int i = 1; i <= n; i++) {
            int x = i;
            bool valid = true;
            bool different = false;

            while (x > 0) {
                int digit = x % 10;

                // Invalid after rotation
                if (digit == 3 || digit == 4 || digit == 7) {
                    valid = false;
                    break;
                }

                // These digits change after rotation
                if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
                    different = true;
                }

                x /= 10;
            }

            if (valid && different) {
                count++;
            }
        }

        return count;
    }
};
