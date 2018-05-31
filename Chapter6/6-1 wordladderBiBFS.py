"""
Author: Huahua
Running time: 115 ms (better than 96.84%)
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict: return 0

        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        wordDict.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()
            for w in s1:
                new_words = [
                    w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in list(range(l))]
                for new_word in new_words:
                    if new_word in s2: return step + 1
                    if new_word not in wordDict: continue
                    wordDict.remove(new_word)
                    s.add(new_word)
            s1 = s

        return 0