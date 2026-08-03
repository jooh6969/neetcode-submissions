class Solution:

    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        # we are going to encode the string in this format
        # <length> <delimiter> <content based on length>
        ans = ""
        for s in strs:
            strLen = len(s)
            ans = ans + str(strLen) + self.delimiter + s
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.delimiter:
                j += 1
            length = int(s[i:j])
            tmp = s[j + 1: length + j + 1]
            ans.append(tmp)
            i = length + j + 1
        return ans