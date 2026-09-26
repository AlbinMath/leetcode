class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int n = nums.size();

        long long sum = 0;
        long long F = 0;

        // Calculate sum of all elements and F(0)
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            F += (long long)i * nums[i];
        }

        long long ans = F;

        // Calculate F(1), F(2), ..., F(n-1)
        for (int k = 1; k < n; k++) {
            F = F + sum - (long long)n * nums[n - k];
            ans = max(ans, F);
        }

        return (int)ans;
    }
};
