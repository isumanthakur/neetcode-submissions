class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr1 = []
        for i in range(len(arr)):
            mx = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > mx:
                    mx = arr[j]
            arr1.append(mx)
        return arr1
        