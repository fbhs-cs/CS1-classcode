"""TODO: 2-Factor Authentication
   ADD A PASSWORD BEFORE THE PIN
   CAN BE ENTERED
   
   Add another while loop so that
   they do nott even get to type in a PIN
   until they get the password right."""

pin = 12345
print("WELCOME TO THE BANK OF PYTHON.")
entry = int(input("ENTER YOUR PIN: "))

while entry != pin:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: "))

print("\nPIN ACCEPTED. YOUR ACCOUNT BALANCE IS $1031.17")
