class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create empty dict/hashmap
        hashmap = {}

        # for each num in the list of nums ...
        for i, num in enumerate(nums):
            
            # create the complement 
            complement = target - num
            
            # [1] if the complement is in the hashmap ... 
            if complement in hashmap:
                # ... and if the current index is not the stored complement's index ... 

                if (i != hashmap[complement]):

                    # ... return the complement's index and the current index.
                    return [hashmap[complement],i]

            # [1] else, save the current index with its current number as the key.
            hashmap[num] = i