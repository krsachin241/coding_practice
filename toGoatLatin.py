# You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
# For example, the word "apple" becomes "applema".
# If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
# Return the final sentence representing the conversion from sentence to Goat Latin.


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
            


                


