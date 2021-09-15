def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    compressed = []
    i, j = 0, 1
    while i <= len(chars):
        if i < len(chars)-1:
            if chars[i] != chars[i+1]:
                ex_pos = j
                j = i+1
                compressed.append(chars[i])
                compressed.append(j - ex_pos + 1)
                i+=1
        if i == len(chars) -1:
            compressed.append(chars[i])
            compressed.append(j - ex_pos + 1)
        i+=1
    print(compressed)

chars =  ["a","a","b","b","c","c","c"]
compress(chars)