class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter=defaultdict(int)

        for i in bills:
            counter[i]+=1

            if i==10:
                if counter[5]>0:
                    counter[5]-=1
                else:
                    return False
            elif i==20:
                if counter[5]>0 and counter[10]>0:
                    counter[5]-=1
                    counter[10]-=1
                elif counter[5]>=3:
                    counter[5]-=3
                else:
                    return False
        
        return True