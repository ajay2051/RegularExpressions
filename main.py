import re

text_to_match = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
corey-ms.com
321-555-4321
123.555.1234
800-154-789
900.457.589
Mr. Schafer
Mr Smith
Mr Davis
Ms Lana
Mrs. Robinson
"""
sentence = "Start a sentence"

print('\tTab')
print(r'\tTab')
pattern = re.compile(r"\d{3}[-.]\d{3}[-.]\d{4}")  # [-.] matches either - or .
pattern_2 = re.compile(r"[89]00[-.]\d{3}[-.]\d{3}")  # 800 or 900-123.456
pattern_3 = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")
matches = pattern_3.finditer(text_to_match)
# matches = pattern_3.findall(text_to_match)
for match in matches:
    print(match)
# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

# pattern = re.compile(r"Start")
# pattern = re.compile(r"start", re.IGNORECASE)
# print(pattern.match(sentence))
# print(pattern.search(sentence))
