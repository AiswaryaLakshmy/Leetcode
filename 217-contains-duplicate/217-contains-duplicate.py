class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
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
            
        