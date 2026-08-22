def roman(s):
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    for i in range(len(s)):
        if s[i] not in d:
            return "Invalid"

    v = 0

    for i in range(len(s)):
        if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
            v -= d[s[i]]
        else:
            v += d[s[i]]

    # Validate by converting back
    r = ""
    n = v
    a = [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'),
         (100,'C'), (90,'XC'), (50,'L'), (40,'XL'),
         (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]

    for x, c in a:
        while n >= x:
            r += c
            n -= x

    if r != s:
        return "Invalid"

    return v


print(roman("XIV"))
print(roman("IIII"))
print(roman("MCM"))