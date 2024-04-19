a = int(input("Choose number between 1 and 10: "))
if 1 <= a <= 10:
    print("Your number is "+ str(a))
while 1 > a or a > 11:
    print("Are you retarded?")
    a = int(input("Try again: "))
    if 1 <= a <= 10:
        print("Finally, your number is " + str(a))
        print("Smart ass nigga")