# O(nm)
def string_matching(T, P):  # T: 입력 문자열, P: 탐색 패턴
    n = len(T)
    m = len(P)

    for i in range(n - m + 1):
        j = 0
        while j < m and P[j] == T[i + j]:
            j += 1
        if j == m:
            return i
    return -1


if __name__ == '__main__':
    print(string_matching("HELLO WORLD", "LO"))
    print(string_matching("HELLO WORLD", "HI"))
