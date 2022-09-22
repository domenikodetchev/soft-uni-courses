quantity = int(input())
days = int(input())
budget = 0
spirit = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += (2 * quantity)
        spirit += 5
    if day % 3 == 0:
        budget += (8 * quantity)
        spirit += 13
    if day % 5 == 0:
        budget += (15 * quantity)
        spirit += 17
    if day % 10 == 0:
        budget += 23
        spirit -= 20
        if day == days:
            spirit -= 30
    if day % 15 == 0:
        spirit += 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
