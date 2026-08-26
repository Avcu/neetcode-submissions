from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diffIsOneChar(str1, str2):
            diffCount = 0
            for idx in range(len(str1)):
                if str1[idx] != str2[idx]:
                    diffCount += 1
                if diffCount == 2:
                    return False
            return diffCount == 1

        
        seen = set()
        q = deque()

        q.append([beginWord, 1])
        seen.add(beginWord)

        while q:
            poppedStr, dist = q.popleft()

            for currStr in wordList:
                if currStr not in seen and diffIsOneChar(poppedStr, currStr):
                    if currStr == endWord:
                        return dist+1
                    else:
                        q.append([currStr, dist+1])
                        seen.add(currStr)
        return 0