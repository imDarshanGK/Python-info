List = list('PYTHON')
values = (List[0], List[1:3]) 
last_two = List[-2:]  # Taking the last two characters
list_length = len(List)  # Getting the length of the list

print('v1={0}, v2={1}, last_two={2}, list_length={3}'.format(*values, last_two, list_length))
