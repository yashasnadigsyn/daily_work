def isIsomorphic(s: str, t: str) -> bool:
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

print(isIsomorphic("egg", "add"))