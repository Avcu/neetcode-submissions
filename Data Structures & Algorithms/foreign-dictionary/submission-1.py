class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def findLink(s1: str, s2: str):
            n1, n2 = len(s1), len(s2)

            idx = 0
            while idx < min(n1, n2) and s1[idx] == s2[idx]:
                idx += 1
            
            if idx < min(n1, n2):
                return [s1[idx], s2[idx]]
            else:
                if idx == n1:
                    return ["", ""]
                else:
                    return [None, None]

        uniqueChars = set()
        inDegree = defaultdict(int)
        for w in words:
            for ch in w:
                if ch not in uniqueChars:
                    uniqueChars.add(ch)
                    inDegree[ch] = 0


        adj = defaultdict(list)
        for idx in range(1, len(words)):
            a, b = findLink(words[idx-1], words[idx])
            if a is None:
                return ""
            if a == "":
                continue
            adj[a].append(b)
            inDegree[b] += 1

        # Topological Sort
        stack = []
        for k, v in inDegree.items():
            if v == 0:
                stack.append(k)

        resStr = ""
        while stack:
            cur = stack.pop()
            resStr += cur

            for nei in adj[cur]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    stack.append(nei)
        
        return resStr if len(resStr) == len(inDegree) else ""







