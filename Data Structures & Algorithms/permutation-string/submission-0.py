class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        c1={}
        for i in s1:
            c1[i]=c1.get(i,0)+1
        
        j=0
        c2={}
        for i in range(len(s2)):
            c2[s2[i]]=c2.get(s2[i],0)+1

            if i-j+1>k:
                c2[s2[j]]-=1
                if c2[s2[j]]==0:
                    c2.pop(s2[j])
                j+=1

            if c1==c2:
                return True

        return False