dials = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

def me(digits):
    def dfs(digits: list[str], ret) -> list[int]:
        if not digits:
            return ret
        
        if len(digits) == 1:
            return list(dials[digits[0]])
        else:
            ret_ = dfs(digits[1:], [])
            r = []
            for c in ret_:
                for d in dials[digits[0]]:
                    r.append(c + d)
            return r
        
    ret = dfs(list(reversed(digits)), [])
    print(ret)
    
def teacher(digits):
    ret = []
    def dfs(index: int, path: str):
        if len(digits) == len(path):
            ret.append(path)
            return
        
        for i in range(index, len(digits)):
            for j in dials[digits[i]]:
                dfs(i + 1, path + j)
    
    if not digits:
        return []
    
    dfs(0, "")
    print(ret)
    
teacher("23")
teacher("5")