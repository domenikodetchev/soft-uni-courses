word = input()
word = word.lower()
n = 0
wordy = ""
lis = []
if word.__contains__("sun"):
    lis = word.split("sun", 1)
    n += 1
elif word.__contains__("sand"):
    lis = word.split("sand", 1)
    n += 1
elif word.__contains__("water"):
    lis = word.split("water", 1)
    n += 1
elif word.__contains__("fish"):
    lis = word.split("fish", 1)
    n += 1
for i in lis:
    if i.__contains__("sun"):
        n += 1
    if i.__contains__("sand"):
        n += 1
    if i.__contains__("water"):
        n += 1
    if i.__contains__("fish"):
        n += 1
print(n)
