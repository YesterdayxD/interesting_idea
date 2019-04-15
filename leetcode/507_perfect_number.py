class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        aSum = 0
        for i in range(1, num):
            if num % i == 0 and i * i < num:
                aSum += i
                aSum += num / i
            if i * i > num:
                break

        return aSum - num == num


if __name__ == '__main__':
    sulo = Solution()
    print(sulo.checkPerfectNumber(28))
