
from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        arr.sort(reverse=True)
        return arr[0]
