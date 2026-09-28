class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, int> rows;

        // Store reserved seats as a bitmask for each row
        for (auto &seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];

            rows[row] |= (1 << col);
        }

        // Rows without reservations can fit 2 groups
        long long ans = 2LL * (n - rows.size());

        for (auto &[row, mask] : rows) {
            // Seats 2,3,4,5
            bool left = (mask & ((1 << 2) |
                                (1 << 3) |
                                (1 << 4) |
                                (1 << 5))) == 0;

            // Seats 4,5,6,7
            bool middle = (mask & ((1 << 4) |
                                   (1 << 5) |
                                   (1 << 6) |
                                   (1 << 7))) == 0;

            // Seats 6,7,8,9
            bool right = (mask & ((1 << 6) |
                                  (1 << 7) |
                                  (1 << 8) |
                                  (1 << 9))) == 0;

            if (left && right) {
                // Two non-overlapping groups
                ans += 2;
            }
            else if (left || middle || right) {
                // Only one group can fit
                ans += 1;
            }
        }

        return (int)ans;
    }
};
