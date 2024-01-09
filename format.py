'''
Format string
'''
str1 = 123
str2 = f"str2: {str1}" # first way
str3 = "str3: {}".format(str1) # second way

print(str2, str3, "str4 {}".format(str1))