
def toGoatLatin(sentence):
    arr = list(map(str, sentence.split()))
    a = 'maa'
    vowel = 'aieouAEIOU'
    lst = []
    for s in arr:
        
        arr1 = [str(i) for i in s]
        
        if arr1[0] not in vowel:
            st = arr1.pop(0)
            arr1.append(st)
            arr1+=a
            a+='a'
            lst.append(arr1)
        else:
            arr1+=a
            lst.append(arr1)
            a+='a'
    res = []
    for i in lst:
        x = ''.join(i)
        res.append(x)
    y = ' '.join(res)
    return y

print(toGoatLatin(sentence = "I speak Goat Latin"))
            


                


