class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def w_of_w(w):
            total = 0
            for c in w:
                index = ord(c) - ord('a')
                total += weights[index]
            return total
        ans = []
        for w in words:
            w_weight = w_of_w(w)
            c = w_weight % 26
            val = ord('z') - c
            ans.append(chr(val))
        return "".join(ans)


        