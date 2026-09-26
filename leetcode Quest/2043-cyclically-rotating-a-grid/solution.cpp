class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        for (int layer = 0; layer < min(m, n) / 2; layer++) {
            vector<int> elements;

            int top = layer;
            int bottom = m - 1 - layer;
            int left = layer;
            int right = n - 1 - layer;

            // Top row
            for (int j = left; j <= right; j++)
                elements.push_back(grid[top][j]);

            // Right column
            for (int i = top + 1; i <= bottom; i++)
                elements.push_back(grid[i][right]);

            // Bottom row
            for (int j = right - 1; j >= left; j--)
                elements.push_back(grid[bottom][j]);

            // Left column
            for (int i = bottom - 1; i > top; i--)
                elements.push_back(grid[i][left]);

            int len = elements.size();
            int shift = k % len;

            int idx = 0;

            // Top row
            for (int j = left; j <= right; j++)
                grid[top][j] = elements[(idx++ + shift) % len];

            // Right column
            for (int i = top + 1; i <= bottom; i++)
                grid[i][right] = elements[(idx++ + shift) % len];

            // Bottom row
            for (int j = right - 1; j >= left; j--)
                grid[bottom][j] = elements[(idx++ + shift) % len];

            // Left column
            for (int i = bottom - 1; i > top; i--)
                grid[i][left] = elements[(idx++ + shift) % len];
        }

        return grid;
    }
};
