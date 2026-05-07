class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]": "[", "}": "{"}

        for cha in s:

            if cha in closeToOpen:
                if stack and stack[-1] == closeToOpen[cha]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cha)
                
        
        return len(stack) == 0
        