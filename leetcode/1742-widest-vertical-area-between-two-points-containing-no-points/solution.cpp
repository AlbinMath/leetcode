
class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> x;

        // Extract x-coordinates
        for (auto& point : points) {
            x.push_back(point[0]);
        }

        // Sort x-coordinates
        sort(x.begin(), x.end());

        int maxWidth = 0;

        // Find the largest gap between adjacent x-coordinates
        for (int i = 1; i < x.size(); i++) {
            maxWidth = max(maxWidth, x[i] - x[i - 1]);
        }

        return maxWidth;
    }
};

