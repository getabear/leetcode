class Solution:
    def simplifyPath(self, path: str) -> str:
        ret=[]
        path=path.split("/")
        for item in path:
            if item=='..':
                if ret:
                    ret.pop()
            elif item and item!='.':
                ret.append(item)
        return '/'+'/'.join(ret)
