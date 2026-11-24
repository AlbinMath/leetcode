class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        int K = min(k, m + n - 1);

        // dp[j][c] = maximum score at column j
        // using exactly cost c.
        vector<vector<int>> dp(n, vector<int>(K + 1, -1));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                int value = grid[i][j];
                int cost = (value == 0 ? 0 : 1);
                int score = value;

                vector<int> cur(K + 1, -1);

                // Starting cell
                if (i == 0 && j == 0) {
                    if (cost <= K)
                        cur[cost] = score;
                } 
                else {
                    // From top
                    for (int c = cost; c <= K; c++) {
                        if (dp[j][c - cost] != -1) {
                            cur[c] = max(
                                cur[c],
                                dp[j][c - cost] + score
                            );
                        }
                    }

                    // From left
                    if (j > 0) {
                        for (int c = cost; c <= K; c++) {
                            if (dp[j - 1][c - cost] != -1) {
                                cur[c] = max(
                                    cur[c],
                                    dp[j - 1][c - cost] + score
                                );
                            }
                        }
                    }
                }

                dp[j] = move(cur);
            }
        }

        int ans = -1;

        for (int c = 0; c <= K; c++) {
            ans = max(ans, dp[n - 1][c]);
        }

        return ans;
    }
};
