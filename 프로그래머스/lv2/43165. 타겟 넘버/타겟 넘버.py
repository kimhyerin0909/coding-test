def solution(numbers, target):
    leaves = [0]
    count = 0
    
    for i in numbers:
        sub = []
        for j in leaves:
            sub.append(j+i)
            sub.append(j-i)
        leaves = sub
    
    return leaves.count(target)