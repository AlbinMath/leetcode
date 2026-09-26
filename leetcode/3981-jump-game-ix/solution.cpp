class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();

        vector<int> ans(n);
        vector<int> preMax(n);

        // Prefix maximum
        preMax[0] = nums[0];

        for (int i = 1; i < n; i++) {
            preMax[i] = max(preMax[i - 1], nums[i]);
        }

        // Traverse from right to left
        int sufMin = INT_MAX;

        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1 || preMax[i] <= sufMin) {
                ans[i] = preMax[i];
            } else {
                ans[i] = ans[i + 1];
            }

            // Important: update AFTER processing i
            sufMin = min(sufMin, nums[i]);
        }

        return ans;
    }
};
