import re

test_string = "123abc456789abc123ABC"

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)  # r means raw string
# matches = pattern.findall(test_string)
for match in matches:
    print(match)
