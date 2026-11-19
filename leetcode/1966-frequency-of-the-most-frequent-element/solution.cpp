#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int left = 0;
        long long window_sum = 0;
        
        for (int right = 0; right < n; ++right) {
            window_sum += nums[right];
            
            // Preserve the widest valid window seen so far
            if (static_cast<long long>(nums[right]) * (right - left + 1) - window_sum > k) {
                window_sum -= nums[left++];
            }
        }
        
        return n - left;
    }
};
