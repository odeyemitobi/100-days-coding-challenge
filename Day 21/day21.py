def solution(string):
    string = list(string)
    string.reverse()
    return ''.join(string)

print(solution("hello"))