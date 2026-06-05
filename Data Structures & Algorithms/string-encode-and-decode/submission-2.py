class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        sizes = []
        res = []
        for i in range(len(strs)):
            sizes.append(len(strs[i]))
        for sz in sizes:
            res.append(str(sz)),
            res.append(',')
        res = res[:-1]
        res.append("\s")
        res.extend(strs)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s: return []
        sizes, res, i = [], [], 0
        print(s.split("\s"))
        sizes, strings = s.split("\s")
        sizes = [int(size) for size in sizes.split(",")]
        ans = []
        for size in sizes:
            ans.append(strings[i: i + size])
            i += size
        return ans