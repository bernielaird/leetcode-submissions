class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        for i in range(len(newStr) // 2):
            if newStr[i] != newStr[-i - 1]:
                return False
        return True