class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_tam = min(len(word1), len(word2))
        answer = [""] * (min_tam * 2)
        index = 0

        for i in range(min_tam):
            answer[index] = word1[i]
            answer[index+1] = word2[i]
            
            index += 2
        
        answer = "".join(answer)

        if len(word1) > len(word2):
            answer += word1[min_tam:]
        elif len(word2) > len(word1):
            answer += word2[min_tam:]
        


        return answer