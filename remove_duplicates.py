

def remove_duplicates(s):
    seen = set()
    results = []
    for char in s:
        if char not in seen:
            seen.add(char)
            results.append(char)
    return ' '.join(results)

print(remove_duplicates("Hello"))