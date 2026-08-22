class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        def generateNeighbors(word):
            chars = [char for char in word]
            st = set()
            for i, char in enumerate(chars):
                for j in range(26):
                    replacement = chr(j + 97)
                    if replacement == char: continue 
                    chars[i] = replacement
                    st.add("".join(chars))
                chars[i] = char
            return st
        hm = {}
        # for i, word in enumerate(wordList):
        #     hm[word] = generateNeighbors(word)
        # hm[beginWord] = generateNeighbors(beginWord)
        # print(hm.keys())
        queue = deque([(beginWord, 1)])
        # potential = set(wordList)
        visited = set([beginWord])
        while queue:
            curr, count = queue.popleft()
            # if curr in visited: continue
            if curr == endWord: return count
            hm[curr] = generateNeighbors(curr)
            for word in wordList:
                toRemove = []
                if word in hm[curr] and word not in visited:
                    visited.add(word)
                    queue.append((word, count + 1))
            # if not potential: continue
            # for word in toRemove:
            #     potential.remove(word)
        return 0