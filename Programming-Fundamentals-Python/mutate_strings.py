first_string = input()
second_string = input()
new_string_list = list(first_string)
new_string_list_2 = list(second_string)
new_string = first_string
for i in range(0, len(second_string)):

    new_string_list[i] = new_string_list_2[i]
    if new_string != "".join(new_string_list):
        print("".join(new_string_list))
    new_string = "".join(new_string_list)


