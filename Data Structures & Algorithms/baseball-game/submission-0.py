class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = []

        for operation in operations:

            if operation == "+":
                answer.append(answer[-1]+answer[-2])
            elif operation == "D":
                answer.append(answer[-1] * 2)
            elif operation == "C":
                answer.pop()
            else:
                answer.append(int(operation))




        return sum(answer) if len(answer) > 0 else 0