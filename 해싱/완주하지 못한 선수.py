from collections import defaultdict

def solve(participant, completion):
    people = defaultdict(int)
    for name in participant:
        people[name] += 1
    for name in completion:
        people[name] -= 1
        if people[name] == 0:
            del people[name]
    
    return next(iter(people))
    

if __name__ == "__main__":
    print(solve(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solve(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solve(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))