def solution(n, words):
    memory = []
    prev = ""
    
    for i in range(len(words)):
        if words[i][0] != prev and i != 0 or words[i] in memory : return (i % n + 1, int(i / n) + 1)
        memory.append(words[i])
        prev = words[i].strip()[-1]
    
    return (0, 0)