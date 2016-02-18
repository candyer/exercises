
# leetcode 4- Median of Two Sorted Arrays

# There are two sorted arrays nums1 and nums2 of size m and n respectively. 
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    new_list = nums1 + nums2
    new_list.sort()
    if len(new_list) % 2 == 0:
        return (new_list[len(new_list) / 2 -1 ] + new_list[len(new_list) / 2])/2.0
    else:
        return new_list[len(new_list) / 2]

print findMedianSortedArrays([2,3,4,6],[1,5,8,10]) #4.5
print findMedianSortedArrays([2,3,4,6],[1,5,8,10,11]) # 5
print findMedianSortedArrays([2,3,3,3],[1,5,5,5,11]) #3
