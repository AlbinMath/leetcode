class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        const int MAX = 2048;

        // Values that actually exist in nums
        vector<bool> present(MAX, false);

        for (int x : nums)
            present[x] = true;

        // All possible XORs of two elements.
        // Repetition is allowed because i <= j <= k.
        vector<bool> pairXor(MAX, false);

        for (int a = 0; a < MAX; a++) {
            if (!present[a])
                continue;

            for (int b = 0; b < MAX; b++) {
                if (!present[b])
                    continue;

                pairXor[a ^ b] = true;
            }
        }

        // Add the third element.
        vector<bool> result(MAX, false);

        for (int x = 0; x < MAX; x++) {
            if (!pairXor[x])
                continue;

            for (int c = 0; c < MAX; c++) {
                if (!present[c])
                    continue;

                result[x ^ c] = true;
            }
        }

        int ans = 0;

        for (bool x : result) {
            if (x)
                ans++;
        }

        return ans;
    }
};
