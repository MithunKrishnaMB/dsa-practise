class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        times=[]
        stack=[]
        
        for i in range(len(position)):
            cars+=[(position[i], speed[i])]
        
        cars.sort(reverse=True)

        for i,j in cars:
            time=(target-i)/j
            times+=[time]
        
        for i in times:
            if not stack:
                stack.append(i)
            elif stack[-1]>=i:
                continue   
            else:
                stack.append(i)
        

        return len(stack)