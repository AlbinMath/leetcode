// The API is already defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isBadVersion(mid)) {
                // mid is bad, so answer is mid or before
                right = mid;
            } else {
                // mid is good, so answer is after mid
                left = mid + 1;
            }
        }

        return left;
    }
};
