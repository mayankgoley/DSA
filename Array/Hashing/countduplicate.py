def countindexduplicate(s):
    count = {}

    for char in s:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1

    i = 0
    while i < len(s):
        if count[s[i]] == 1:
            return i
        i +=1
    return -1

s = "loveleetcode"
print(countindexduplicate(s))