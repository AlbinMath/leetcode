class Solution {
    func maximumLengthSubstring(_ s: String) -> Int {
        let chars = Array(s)
        var count = [Int](repeating: 0, count: 26)
        
        var left = 0
        var ans = 0
        
        for right in 0..<chars.count {
            let index = Int(chars[right].asciiValue! - Character("a").asciiValue!)
            count[index] += 1
            
            while count[index] > 2 {
                let leftIndex = Int(chars[left].asciiValue! - Character("a").asciiValue!)
                count[leftIndex] -= 1
                left += 1
            }
            
            ans = max(ans, right - left + 1)
        }
        
        return ans
    }
}
