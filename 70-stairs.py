class Solution:
    def climbStairs(self, n: int) -> int:
        #solution is fib series
        array = [0] * (n + 1)
        array[0] = 1
        array[1] = 1
        # print(array)
        
        for i in range(2, n + 1):
            array[i] = array[i-1] + array[i-2]
        
        # print(array)
        
        return array[n]