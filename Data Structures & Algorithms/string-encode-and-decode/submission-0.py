class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for item in strs:
            final_str += item
            final_str += "ğ" # Seperate items with ğ
        return final_str
    def decode(self, s: str) -> List[str]:
        listo = []
        temp = ""
        for char in s:
            print(char)
            if char == "ğ": # We hit a new word
                listo.append(temp)
                temp = ""
            else:
                temp += char
        return listo