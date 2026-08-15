class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        sim_path="/"
        name=""

        for i in path:
            if i=="/":
                if name=="":
                    continue        
                
                if name=="..":
                    if stack:
                        stack.pop()
                elif name!=".":
                    stack.append(name)
                
                name=""
            else:
                name+=i
        
        if name=="..":
            if stack:
                stack.pop()        
        elif name!="" and name!=".":
            stack.append(name)

        for i in range(len(stack)):
            sim_path+=stack[i]

            if i<len(stack)-1:
                sim_path+="/"
        
        return sim_path