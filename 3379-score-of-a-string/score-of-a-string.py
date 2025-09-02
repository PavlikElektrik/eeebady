class Solution:
    #aboba
    def scoreOfString(self, s: str) -> int:
        ascii_values = [ord(char) for char in s]
        return sum(abs(ascii_values[i] - ascii_values[i+1]) for i in range(len(s)-1))
