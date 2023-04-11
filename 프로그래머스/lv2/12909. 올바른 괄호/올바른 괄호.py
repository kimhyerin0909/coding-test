def solution(s):
    arr = list(s)
    stack = [arr[0]]
    if arr.count("(") != arr.count(")") : return False
    for i in range(1, len(arr)):
        if len(stack) > 0 and stack[-1] == "(" and arr[i] == ")": stack.pop()
        elif arr[i] == "(": stack.append(arr[i])
    return len(stack) < 1