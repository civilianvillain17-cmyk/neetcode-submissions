class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack: # Если не пустой
                    return False
                top = stack.pop() # Последний элемент списка
                if top != pairs[ch]:
                    return False
        return not stack # В случае удачного завершения список должен быть пустой
                