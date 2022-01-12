

'''
anagrams are those words which can give the same words when reaaranged. eg: god, dog are anagrams etc 
'''

def anagram(s, t):

    s = s.replace(" ","").lower()
    t = t.replace(" ","").lower()

    if len(s) != len(t):
        return False

    counter = {}

    for letter in s:

        if letter in counter:
            counter[letter] += 1

        else:

            counter[letter] = 1

    for letter in t:

        if letter in counter:
            counter[letter] -= 1

        else:
            return False

    for k in counter:

        if counter[k] != 0:
            return False

    return True

a = anagram('go go go','gggooo')

print(a)