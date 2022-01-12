'''

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

'''


# The trick is to add a number if it is greater than the previous number. If the previous no is less tahn the next no. then we subtract it

s = input()

roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

z = 0

for i in range(0, len(s)-1):

    if roman[s[i]] < roman[s[i+1]]:
        
        z -= roman[s[i]]

    else:

        z += roman[s[i]]

print(z + roman[s[-1]])