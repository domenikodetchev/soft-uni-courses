budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = flour_price * 1.25
loafs = 0
eggs = 0
loaf_price = flour_price + egg_price + (0.25 * milk_price)
while budget - loaf_price > 0:
    loafs += 1
    eggs += 3
    if loafs % 3 == 0:
        eggs -= (loafs - 2)
    budget -= loaf_price
print(f"You made {loafs} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
