class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        vector<int> prefixGcd;
        int mx = 0;

        // Construct prefixGcd
        for (int x : nums) {
            mx = max(mx, x);
            prefixGcd.push_back(gcd(x, mx));
        }

        // Sort prefixGcd
        sort(prefixGcd.begin(), prefixGcd.end());

        // Pair smallest with largest
        long long ans = 0;
        int left = 0;
        int right = prefixGcd.size() - 1;

        while (left < right) {
            ans += gcd(prefixGcd[left], prefixGcd[right]);
            left++;
            right--;
        }

        return ans;
    }
};
