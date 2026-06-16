class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                push=1

                while stack and i<0 and stack[-1]>0:
                    if abs(i)==abs(stack[-1]):
                        stack.pop()
                        push=0
                        break
                    elif abs(i)>abs(stack[-1]):
                        stack.pop()
                    else:
                        push=0
                        break
                
                if push==1:
                    stack.append(i)
        return stack