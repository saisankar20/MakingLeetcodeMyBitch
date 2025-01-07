class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += f"{len(i)}#{i}"
        return encoded_str

            
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j =s.find('#', i)
            length = int(s[i:j])

            decoded.append(s[j+1 :j+1 +length])

            i = j + 1 + length

        return decoded
