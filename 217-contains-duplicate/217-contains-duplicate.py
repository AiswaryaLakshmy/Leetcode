class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) != len(set(nums))
        '''
        temp = []
        if not nums or len(nums) == 0:
            return False

        for i in nums:
            if i in temp:
                return True
            temp.append(i)
        else:
            return False
        
        '''
        h = {}
        for idx, val in enumerate(nums):
            if val in h:
                return True
            else:
                h[val] = idx
        return False
        