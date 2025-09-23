class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        #track values from bottom up
        forward = 0

        # track values from the target 'n' and backwards from thre
        backward = n
        for i in range(n):
            if '0' not in str(forward) and '0' not in str(backward):
                if forward + backward == n:
                    return [forward, backward]
            forward += 1
            backward -= 1

        
        