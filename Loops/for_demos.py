count = 0
for val in range(1,100):
    if val % 5 == 0:
        count += 1
    if count == 5:
        print(val)
        break
    
