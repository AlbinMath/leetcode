class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();

        // Store {value, original index}
        vector<pair<int, int>> arr;

        for (int i = 0; i < n; i++) {
            arr.push_back({nums[i], i});
        }

        // Sort by value
        sort(arr.begin(), arr.end());

        vector<int> ans(n);

        int i = 0;

        while (i < n) {
            int j = i;

            // Find the connected group
            while (j + 1 < n &&
                   arr[j + 1].first - arr[j].first <= limit) {
                j++;
            }

            // Get original indices of this group
            vector<int> indices;

            for (int k = i; k <= j; k++) {
                indices.push_back(arr[k].second);
            }

            // Sort original indices
            sort(indices.begin(), indices.end());

            // Values are already sorted
            // Assign smallest values to smallest indices
            for (int k = 0; k < (int)indices.size(); k++) {
                ans[indices[k]] = arr[i + k].first;
            }

            i = j + 1;
        }

        return ans;
    }
};
