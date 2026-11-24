
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int minDistance = INT_MAX;
        int result = -1;

        for (int i = 0; i < points.size(); i++) {
            int a = points[i][0];
            int b = points[i][1];

            // Check whether the point is valid
            if (a == x || b == y) {
                int distance = abs(x - a) + abs(y - b);

                if (distance < minDistance) {
                    minDistance = distance;
                    result = i;
                }
            }
        }

        return result;
    }
};

