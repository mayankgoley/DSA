def countuniquechar(s):
    count = {}

    for char in s:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i
        
    return -1

s = "loveleetcode"
print(countuniquechar(s))