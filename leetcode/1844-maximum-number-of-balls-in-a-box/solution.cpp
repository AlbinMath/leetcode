
class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        int boxes[50] = {0};

        for (int i = lowLimit; i <= highLimit; i++) {
            int num = i;
            int sum = 0;

            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }

            boxes[sum]++;
        }

        int maxBalls = 0;

        for (int count : boxes) {
            maxBalls = max(maxBalls, count);
        }

        return maxBalls;
    }
};

