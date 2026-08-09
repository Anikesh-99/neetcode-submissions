class Node:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
    
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.child: return False
            curr = curr.child[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.child: return False
            curr = curr.child[c]
        return True
        
        