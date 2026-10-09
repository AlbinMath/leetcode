
class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int freq[101] = {0};

        // Count the frequency of each number
        for (int num : nums) {
            freq[num]++;
        }

        int sum = 0;

        // Add elements that appear exactly once
        for (int num : nums) {
            if (freq[num] == 1) {
                sum += num;
            }
        }

        return sum;
    }
};

