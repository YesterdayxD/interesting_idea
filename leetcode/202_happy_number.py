class Solution(object):
    """
    Write an algorithm to determine if a number is "happy".

    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by
     the sum of the squares of its digits, and repeat the process
     until the number equals 1 (where it will stay), or it loops endlessly
     in a cycle which does not include 1. Those numbers for
     which this process ends in 1 are happy numbers.
    """

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        noRepeat = []
        while True:
            n_p = list(map(int, str(n)))
            n_p = sum([i * i for i in n_p])
            if n_p in noRepeat:
                return False
            if n_p == 1:
                return True

            noRepeat.append(n_p)
            print(n_p)
            n = n_p
        return True


if __name__ == '__main__':
    solu = Solution()
    print(solu.isHappy(19))
