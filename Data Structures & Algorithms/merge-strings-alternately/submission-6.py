class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        i, j = 0, 0
        n, m = len(word1), len(word2)

        while i < n or j < m:
            if i < n:
                output = output + word1[i]
                i = i + 1
            if j < m:
                output = output + word2[j]
                j = j + 1
            
        return output
                



# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         i = 0
#         output = ""
#         max_l = max([len(word1), len(word2)])

#         while i < max_l:
#             if i < len(word1):
#                 output = output + word1[i]
#             if i < len(word2):
#                 output = output + word2[i]

#             i += 1
            
#         return output