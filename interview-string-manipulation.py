String = 'Interview'
vowels = 'aeiouAEIOU'
new_str = ''.join(['*' if ch in vowels else ch for ch in String])
print(new_str)
