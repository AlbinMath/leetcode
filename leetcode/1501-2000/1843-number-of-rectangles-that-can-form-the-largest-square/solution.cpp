
class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int maxLen = 0;
        int count = 0;

        for (auto& rectangle : rectangles) {
            int side = min(rectangle[0], rectangle[1]);

            if (side > maxLen) {
                maxLen = side;
                count = 1;
            }
            else if (side == maxLen) {
                count++;
            }
        }

        return count;
    }
};

