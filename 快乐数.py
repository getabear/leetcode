class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        slow=n
        fast=get_next(n)
        fast=get_next(fast)
        while(slow!=fast):
            slow=get_next(slow)
            fast=get_next(fast)
            fast=get_next(fast)

        return slow==1
