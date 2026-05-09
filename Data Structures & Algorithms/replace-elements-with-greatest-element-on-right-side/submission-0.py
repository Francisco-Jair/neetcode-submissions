class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [-1]
        biggest = arr[len(arr)-1]

        for i in range(len(arr)-1, 0, -1):
            if arr[i] > biggest:
                answer.append(arr[i])
                biggest = arr[i]
            else:
                answer.append(biggest)
        
        answer.reverse()
        return answer