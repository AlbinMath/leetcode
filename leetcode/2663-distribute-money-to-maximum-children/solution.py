class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        k = min(money // 7, children)
        left = money - 7 * k
        if k == children and left != 0:
            return children - 1
        if k == children - 1 and left == 3:
            return children - 2
        return k
