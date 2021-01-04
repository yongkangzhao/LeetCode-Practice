'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = sorted(wordDict, key = lambda x:-len(x))
        self.memo = {}
        return self.dfs(s)
    
    
    def dfs(self, s):
        if s == '':
            return True
        if s in self.memo:
            return self.memo[s]
        for word in self.wordDict:
            if(s[:len(word)] == word):
                if(self.dfs(s[len(word):])):
                    return True
        self.memo[s] = False
        return False