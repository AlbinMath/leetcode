class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();

        // Difference array for number of moves
        vector<int> diff(2 * limit + 2, 0);

        for (int i = 0; i < n / 2; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];

            int low = min(a, b) + 1;
            int high = max(a, b) + limit;

            int sum = a + b;

            // 1 move is possible for sums in [low, high]
            diff[low]--;
            diff[high + 1]++;

            // 0 moves for exactly 'sum'
            diff[sum]--;
            diff[sum + 1]++;
        }

        int moves = n;
        int current = n;

        for (int s = 2; s <= 2 * limit; s++) {
            current += diff[s];
            moves = min(moves, current);
        }

        return moves;
    }
};
