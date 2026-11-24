
class Solution {
public:
    int total = 0;

    void backtrack(vector<int>& nums, int index, int currentXOR) {
        if (index == nums.size()) {
            total += currentXOR;
            return;
        }

        // Include the current element
        backtrack(nums, index + 1, currentXOR ^ nums[index]);

        // Exclude the current element
        backtrack(nums, index + 1, currentXOR);
    }

    int subsetXORSum(vector<int>& nums) {
        total = 0;
        backtrack(nums, 0, 0);
        return total;
    }
};

