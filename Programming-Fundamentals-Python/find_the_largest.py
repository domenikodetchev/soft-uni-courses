num = input()
num_list = list(num)
num_list.sort(reverse=int(num))
for item in num_list:
    print(item, end="")