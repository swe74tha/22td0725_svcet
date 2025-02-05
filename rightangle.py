n = int(input("enter a row"))
for i in range(1,n+1):
    star = (1*i-1) * " *"  
    space = (n+1) * " "  
    print(star+ space)