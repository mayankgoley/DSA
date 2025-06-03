"""
You are given two sorted arrays:

nums1 of length m + n, where the first m elements are meaningful, and the rest are 0s to hold the second array.
nums2 of length n.
nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]"""



def merge(nums1, m, nums2, n):
    i = len(nums1) -1
    j = len(nums2) -1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            nums2[k] = nums2[i]
            j-=1
            k -=1
        

