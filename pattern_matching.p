import re

text = "xy78mn90gh12"
matches = re.findall(r"([a-z]{2})(\d{2})", text)
print(matches)
