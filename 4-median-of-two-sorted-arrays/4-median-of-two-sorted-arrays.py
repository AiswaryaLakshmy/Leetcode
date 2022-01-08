class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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