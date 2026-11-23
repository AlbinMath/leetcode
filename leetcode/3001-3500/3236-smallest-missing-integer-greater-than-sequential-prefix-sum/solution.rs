impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        let mut sum = nums[0];

        // Find the longest sequential prefix
        for i in 1..nums.len() {
            if nums[i] == nums[i - 1] + 1 {
                sum += nums[i];
            } else {
                break;
            }
        }

        // Find the smallest missing integer >= sum
        let mut ans = sum;

        while nums.contains(&ans) {
            ans += 1;
        }

        ans
    }
}
