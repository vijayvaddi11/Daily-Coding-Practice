from collections import Counter


class Solution:
    def find_unique(self, k, arr):
        freq = Counter(arr)
        for num in arr:
            if freq[num] < k:
                return num 
            