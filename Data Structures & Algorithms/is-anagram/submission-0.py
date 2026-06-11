class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count={}
        t_count={}

        for i in s:
            if s_count.get(i):
                s_count[i]+=1
            else:
                s_count[i]=1
        
        for i in t:
            if t_count.get(i):
                t_count[i]+=1
            else:
                t_count[i]=1
        
        return s_count==t_count