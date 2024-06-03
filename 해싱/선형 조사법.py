M = 13
table = [None] * M

def hashf(key):
    return key % M

def lp_insert(key):
    id = hashf(key)
    remain = M
    
    # -1은 데이터가 있었다가 삭제된 것, None은 아예 있어본 적도 없던 것
    while remain > 0 and table[id] is not None and table[id] != -1:
        id = (id + 1 + M) % M
        remain -= 1
        
    if remain > 0:
        table[id] = key

def lp_search(key):
    id = hashf(key)
    remain = M
    
    while remain > 0:
        if table[id] is None:
            return None
        if table[id] != -1 and table[id] == key:
            return table[id]
        
        id = (id + 1 + M) % M
        remain -= 1
    
    return None

def lp_delete(key):
    id = hashf(key)
    remain = M
    
    while remain > 0:
        if table[id] is None:
            return None
        if table[id] != -1 and table[id] == key:
            table[id] = -1
            return
        
        id = (id + 1 + M) % M
        remain -= 1

if __name__ == "__main__":
    print("최초:", table)
    
    for key in [45, 27, 88, 9, 71, 60, 46, 38, 24]:
        lp_insert(key)
        print(key, "삽입:", table)

    lp_delete(60)
    print("60 삭제:", table)
    
    print("46 탐색:", lp_search(46))
