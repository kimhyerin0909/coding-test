def solution(s):
    y = ""
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ": y = y + s[i].upper()
        else : y = y + s[i].lower()
    return y