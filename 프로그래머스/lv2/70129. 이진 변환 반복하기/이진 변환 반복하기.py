def repeat(s):
    n = s.count("1")
    return bin(n)[2:]

def solution(s):
    count = 0
    zero = 0
    
    while(s != "1"):
        count += 1
        zero += len(s) - s.count("1")
        s = repeat(s)
    return (count, zero)