
class Solution {
public:
    int totalMoney(int n) {
        int money = 0;
        int monday = 1;

        for (int day = 0; day < n; day++) {
            money += monday + day % 7;
            
            if (day % 7 == 6) {
                monday++;
            }
        }

        return money;
    }
};

