class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = defaultdict(int)
        for idx in range(len(order)):
            orderDict[order[idx]] = idx

        def compareTwoWords(s1, s2):
            n, m = len(s1), len(s2)
            for idx in range(min(n,m)):
                ord1, ord2 = orderDict[s1[idx]], orderDict[s2[idx]]
                if ord1 < ord2:
                    return True
                elif ord1 == ord2:
                    continue
                else:
                    return False
            return n <= m


        for idx in range(1, len(words)):
            if not compareTwoWords(words[idx-1], words[idx]):
                return False
        return True