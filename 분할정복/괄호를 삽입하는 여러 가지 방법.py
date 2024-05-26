def solution(expression: str) -> list[int]:
    def calc(lefts: list[int], rights: list[int], op: str) -> list[int]:
        result = []
        for l in lefts:
            for r in rights:
                if op == '+':
                    result.append(l + r)
                elif op == '-':
                    result.append(l - r)
                else:
                    result.append(l * r)
        return result
    
    if expression.isdigit():
        return [int(expression)]
    
    result = []
    for i in range(len(expression)):
        if expression[i] in '+-*':
            left = solution(expression[:i])
            right = solution(expression[i+1:])
            result.extend(calc(left, right, expression[i]))
            
    return result

print(solution("2-1-1"))
print(solution("2*3-4*5"))