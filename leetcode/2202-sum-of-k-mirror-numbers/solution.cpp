class Solution {
public:
    long long kMirror(int k, int n) {
        long long total = 0;
        int count = 0;
        int digits[64];

        auto isBaseKPalindrome = [&](long long x) {
            int len = 0;
            while (x > 0) {
                digits[len++] = x % k;
                x /= k;
            }
            for (int i = 0, j = len - 1; i < j; ++i, --j) {
                if (digits[i] != digits[j]) return false;
            }
            return true;
        };

        for (long long len = 1; count < n; ++len) {
            long long half = (len + 1) / 2;
            long long start = 1;
            for (int i = 1; i < half; ++i) start *= 10;
            long long end = start * 10;

            for (long long p = start; p < end && count < n; ++p) {
                long long pal = p;
                long long temp = (len % 2 == 1) ? (p / 10) : p;
                while (temp > 0) {
                    pal = pal * 10 + (temp % 10);
                    temp /= 10;
                }
                if (isBaseKPalindrome(pal)) {
                    total += pal;
                    ++count;
                }
            }
        }
        return total;
    }
};
