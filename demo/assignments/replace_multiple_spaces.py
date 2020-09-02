import re

f = open("story.txt", "r")
text = f.read()
text = re.sub(r'[ ]+', ' ', text)
text = re.sub(r'[\n]+', r'\n', text)
# print(text)
f.close()

# Write modified content back to file
f = open("story.txt", "w")
f.write(text)
f.close()
