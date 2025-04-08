print("BANK OF CODEDEX")
pin = int(input("Enter your PIN: "))
while pin != 1234: # != is does not equal
  pin = int(input("Incorrect. Try again!:"))
if pin == 1234: # == is equal to in terminal
  print("PIN accepted.")
