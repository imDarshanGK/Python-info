str1 = "abc"
str2 = str1
str1 += "d"
str1 = str1.lower()
print(str1 is str2)
