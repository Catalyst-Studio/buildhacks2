x = 20
forever = True
while forever:
    if x > 50:
        x = x / 2
    elif x < 50:
        x = x * 2
    if x == 50:
        forever = False
    if x > 50:
        x -= 1
    elif x < 50:
        x += 1
print("x = 50")