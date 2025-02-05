X = int(input("enter a year"))
if X % 4 ==0 or X % 400 ==0 & X % 100 ==0:
    print("It is a leap year")
else:
    print("It is not a leap year")