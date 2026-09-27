# @param {Integer} n
# @param {Integer} t
# @return {Integer}
def smallest_number(n, t)
    while true
        x = n
        product = 1

        while x > 0
            product *= x % 10
            x /= 10
        end

        return n if product % t == 0

        n += 1
    end
end
