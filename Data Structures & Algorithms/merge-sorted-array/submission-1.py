class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=m+n-1

        while i<m:
            nums1[j]=nums1[m-1-i]
            i+=1
            j-=1
        
        i=0

        while i<n:
            nums1[i]=nums2[i]
            i+=1
        
        nums1.sort()