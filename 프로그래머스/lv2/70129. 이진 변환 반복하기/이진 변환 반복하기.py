def solution(s):
    count, zero = 0, 0
    
    while(s != "1"):
        count += 1
        zero += len(s) - s.count("1")
        s = bin(s.count("1"))[2:]
    return (count, zero)