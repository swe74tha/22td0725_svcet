a=input("enter the password:")
up=0
sm=0
dg=0
sp=0
if(len(a)>7):
    for i in a:
        if(i.isupper()):
            up=up+1   
        if(i.islower()):
            sm=sm+1 
        if(i.isdigit()):
            dg=dg+1 
        else:
            sp=sp+1 
    if(up>0 and sm>0 and dg>0 and sp>0):
        print("IT IS STRONG PASSWORD :")
    else:
        print("IT IS WEAK PASSWORD:")
else:
    print("WEAK PASSWORD ,PLEASE SATISFY CONDITION:")