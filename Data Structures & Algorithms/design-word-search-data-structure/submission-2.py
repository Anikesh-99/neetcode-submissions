class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
    
    def __repr__(self):
        return f"End of Word: {self.endOfWord}, Children: {self.child.keys()}"

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        end = len(word)
        for i, c in enumerate(word):
            if c not in curr.child: 
                end = i
                break
            curr = curr.child[c]
        for i in range(end, len(word)):
            curr.child[word[i]] = TrieNode()
            curr = curr.child[word[i]]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # print(word)
        curr = self.root
        def helper(node, idx):
            if idx == len(word): 
                # print(f"{idx}, {node}")
                return node.endOfWord
            c = word[idx]
            # print(f"{c}, {node}, {idx}")
            if not node: return False
            if c != ".":
                return c in node.child and helper(node.child[c], idx + 1)
            else:
                isFound = False
                for key, value in node.child.items():
                    isFound = isFound or helper(value, idx + 1)
                    if isFound: return True
                return isFound
        return helper(curr, 0) 

