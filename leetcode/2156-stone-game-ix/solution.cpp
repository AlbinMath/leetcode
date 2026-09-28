class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        int cnt[3] = {0, 0, 0};

        for (int x : stones) {
            cnt[x % 3]++;
        }

        // Stones divisible by 3 do not change the sum's remainder.
        // If there are an even number of them, they can effectively
        // be ignored for the main strategy.
        if (cnt[0] % 2 == 0) {
            return cnt[1] > 0 && cnt[2] > 0;
        }

        // Odd number of 0-mod-3 stones
        return abs(cnt[1] - cnt[2]) > 2;
    }
};
