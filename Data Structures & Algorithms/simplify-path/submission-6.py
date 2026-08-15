class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        name = ""

        for ch in path:
            if ch == "/":
                if name == "":
                    continue

                if name == "..":
                    if stack:
                        stack.pop()
                elif name != ".":
                    stack.append(name)

                name = ""
            else:
                name += ch

        if name == "..":
            if stack:
                stack.pop()
        elif name != "" and name != ".":
            stack.append(name)

        return "/" + "/".join(stack)