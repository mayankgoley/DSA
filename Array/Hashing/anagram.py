def valid_anagram(s):
    seen = {}

    for words in s:
        key= "".join(sorted(words))

        if key not in seen:
            seen[key] = []
        
        seen[key].append(words)

    return list(seen.values())

s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(valid_anagram(s))
