class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        merged_arr = nums1 + nums2
        merged_arr.sort()
        print(merged_arr)
        l = 0
        u = len(merged_arr) - 1
        #print(len(merged_arr))
        #while l<=u:
        mid = (l+u) // 2
        if u % 2 ==0:
            
            return (merged_arr[mid]+0.0)
        else:
            return ((merged_arr[mid] + merged_arr[mid+1])/2)
        '''
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        left = -1
        right = len(nums1)
        half_length = (len(nums1) + len(nums2)) // 2 + (len(nums1) + len(nums2)) % 2

        while left <= right:
            p1 = (left + right) // 2
            if p1 < 0:
                p2 = half_length - 1
            elif p1 >= len(nums1):
                p2 = half_length - len(nums1) - 1
            else:
                p2 = half_length - p1 - 2


            p1_right = nums1[p1 + 1] if p1 < len(nums1) - 1 else math.inf
            p1_left = nums1[p1] if p1 >= 0 else -math.inf
            p2_right = nums2[p2 + 1] if p2 < len(nums2) - 1 else math.inf
            p2_left = nums2[p2] if p2 >= 0 else - math.inf

            if p2_right >= p1_left:
                if p1_right >= p2_left:
                    if (len(nums1) + len(nums2)) % 2 == 0:
                        return (min(p1_right, p2_right) + max(p1_left, p2_left)) / 2.0
                    else: return max(p1_left, p2_left)
                else:
                    left = p1 + 1
            else:
                right = p1 - 1