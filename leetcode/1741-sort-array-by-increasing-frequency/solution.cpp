
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> freq;

        // Count the frequency of each number
        for (int num : nums) {
            freq[num]++;
        }

        // Sort by frequency, then by decreasing value
        sort(nums.begin(), nums.end(), [&](int a, int b) {
            if (freq[a] != freq[b]) {
                return freq[a] < freq[b];
            }
            return a > b;
        });

        return nums;
    }
};

