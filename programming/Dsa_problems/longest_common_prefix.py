
# 14. Longest Common Prefix


def longest_prefix(my_strs):

    prefix = my_strs[0]

    for word in my_strs:

        if len(prefix) > len(word):

            prefix, word = word, prefix

        while len(prefix) > 0:

           if word[:len(prefix)] == prefix:

               break
           else:
               
               prefix = prefix[:-1]

    return prefix


s = ["flower","flow","flight"]
pref = longest_prefix(s)

print(pref)
