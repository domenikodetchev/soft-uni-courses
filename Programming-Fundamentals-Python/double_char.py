word = ""

while word != "End":
    word = input()
    if word == "SoftUni":
        continue
    if word == "End":
        break
    for i in range(0, len(word)):
        if i == len(word) - 1:
            double_char = word[i] + word[i]
            print(double_char)
            break
        double_char = word[i] + word[i]
        print(double_char, end="")
