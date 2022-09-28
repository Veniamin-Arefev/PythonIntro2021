def find(source, pattern):
    for i in range(len(source) - len(pattern) + 1):
        suitable = True
        for j in range(len(pattern)):
            if (pattern[j] != '@') and pattern[j] != source[i+j]:
                suitable = False
                break
        if suitable:
            return i
    return -1


print(find(input(), input()))
