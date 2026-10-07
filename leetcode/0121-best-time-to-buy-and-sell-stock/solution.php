class Solution {
    function maxProfit($prices) {
        $minPrice = PHP_INT_MAX;
        $maxProfit = 0;

        foreach ($prices as $price) {

            // Lowest buying price so far
            $minPrice = min($minPrice, $price);

            // Profit if we sell today
            $profit = $price - $minPrice;

            // Maximum profit so far
            $maxProfit = max($maxProfit, $profit);
        }

        return $maxProfit;
    }
}
