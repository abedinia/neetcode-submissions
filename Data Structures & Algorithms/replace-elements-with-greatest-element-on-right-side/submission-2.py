class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            j = i + 1
            if len(arr[j:]) > 0:
                result.append(max(arr[j:]))
            else:
                result.append(-1)

        return result