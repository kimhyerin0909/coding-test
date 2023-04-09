def solution(brown, yellow):
    yel = int(yellow)
    for i in range(1, yel+1):
        if yel % (i) == 0:
            if (i * 2 + (int(yel / i) * 2) + 4) == brown and i >= int(yel/i):
                return i+2, int(yel / i)+2