class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();
        int diff = 0;
        int q = 0;

        for (int i = 0; i < n / 2; i++) {
            if (num[i] == '?')
                q++;
            else
                diff += num[i] - '0';
        }

        for (int i = n / 2; i < n; i++) {
            if (num[i] == '?')
                q--;
            else
                diff -= num[i] - '0';
        }

        if (q == 0)
            return diff != 0;

        // Each unmatched pair of ? can change the difference
        // by at most 9.
        return abs(q) % 2 == 1 ||
               diff * 2 != -9 * q;
    }
};
