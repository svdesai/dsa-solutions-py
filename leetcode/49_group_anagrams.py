# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = collections.defaultdict(list)
        for curr_string in strs:
            sorted_curr_string = ''.join(sorted(curr_string))
            h[sorted_curr_string].append(curr_string)
        
        return h.values()
