import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            seen.add(char)
            stack.append(char)

        return ''.join(stack)


