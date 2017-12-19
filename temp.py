temperature = 65
while temperature < 80:
    print("It's still a nice day")
    if temperature < 70:
        temperature = temperature + 5
    else:
        temperature = temperature + 3
    
    if temperature > 75:
        break