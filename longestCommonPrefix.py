def longestCommonPrefix(strs):
    st = strs[0]
    s = ''
    for i in range(len(st)):
        for j in range(1, len(strs)):
            
            if i >= len(strs[j]) or st[i]!=strs[j][i]:
                return s 
        s+=st[i]
        
    return s
print(longestCommonPrefix(strs = ["flower","flow","flight"]))
