from collections import deque

items = deque([100, 200, 300, 400])
items.append(500)  # Adding an element to the deque
items.popleft()    # Removing an element from the left side

print(items)
