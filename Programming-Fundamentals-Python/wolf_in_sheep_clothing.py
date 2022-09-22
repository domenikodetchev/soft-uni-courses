sheeps = input()
sheep_list = []
word = ""
for letter in sheeps:
    if letter == " " or letter == ",":
        word = ""
    else:
        word += letter
        if word == "sheep" or word == "wolf":
            sheep_list.append(word)
sheep_list.reverse()
for sheep in sheep_list:
    if sheep == "wolf" and sheep_list.index("wolf") == 0:
        print("Please go away and stop eating my sheep")
    elif sheep == "wolf":
        wolf = sheep_list.index("wolf")
        print(f"Oi! Sheep number {wolf}! You are about to be eaten by a wolf!")
        