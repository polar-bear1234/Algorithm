def replaceSpaces1(S, length):
    return S[:length].replace(' ', '%20')


def replaceSpaces(S, length):
    # 双指针
    S = list(S)
    right = len(S) - 1
    count = 0
    for i in range(length-1, -1, -1):
        if S[i] == ' ':
            count += 2
    L = length + count
    for left in range(length - 1, -1, -1):
        if S[left] != ' ':
            S[right] = S[left]
            right -= 1
        else:
            S[right] = "%"
            S[right - 1] = "0"
            S[right - 2] = "2"
            right -= 3
    return "".join(S[-L:])


str1 = "Mr John Smith    "
str2 = "ds sdfs afs sdfa dfssf asdf             "
length = 27
result = replaceSpaces(str2, length)
print(result)   # ds ds20%sdfs20%afs20%sdfa20%dfssf20%asdf