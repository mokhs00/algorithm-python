# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        list = []

        for str in s:
            if str.isalnum():
                list.append(str.lower())

        return list == list[::-1]
