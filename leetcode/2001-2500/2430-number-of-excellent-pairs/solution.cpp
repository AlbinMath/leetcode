#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    long long countExcellentPairs(vector<int>& nums, int k) {
        // Step 1: Deduplicate nums
        unordered_set<int> unique_nums(nums.begin(), nums.end());
        
        // Step 2: Count frequencies of set bits (max 30 bits for 10^9)
        long long bit_counts[32] = {0};
        for (int num : unique_nums) {
            bit_counts[__builtin_popcount(num)]++;
        }
        
        // Step 3: Sum valid combinations
        long long ans = 0;
        for (int b1 = 0; b1 < 32; ++b1) {
            for (int b2 = 0; b2 < 32; ++b2) {
                if (b1 + b2 >= k) {
                    ans += bit_counts[b1] * bit_counts[b2];
                }
            }
        }
        return ans;
    }
};
