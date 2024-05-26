# brute-force -> 9798ms
def majorityElement(nums: list[int]) -> int:
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num
        
# 분할 정복 -> 218ms
def majorityElement2(nums: list[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    # leetcode에서는 class의 메소드로 답안을 제출하기 때문에 함수 인자에 self가 필요하고, 재귀 호출 시에도 self.majority... 해야 함. 실수 안하겠지 이런건
    a = majorityElement2(nums[:half])
    b = majorityElement2(nums[half:])
    
    return [b, a][nums.count(a) > half]

# 해쉬 테이블 -> 175ms
def majorityElement3(nums: list[int]) -> int:
    D = {}
    for num in nums:
        if num not in D:
            D[num] = 0
        D[num] += 1
        
    for k in D:
        if D[k] > len(nums) // 2:
            return k

# 가장 빠른 풀이 -> 166ms
def majorityElement4(nums: list[int]) -> int:
    return sorted(nums)[len(nums) // 2]

for test_case in ([3, 2, 3], [2, 2, 1, 1, 1, 2, 2]):
    print(f'testcase: {test_case} | ', end='')
    for func in (majorityElement, majorityElement2, majorityElement3, majorityElement4):
        print(func(test_case), end=' ')
    print()