class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        mr = -1
        for i in range(n-1,-1, -1):
            nm = max(mr, arr[i])
            arr[i] =  mr
            mr = nm
        return arr

        