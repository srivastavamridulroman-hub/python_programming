def function(a,b,c):

    if(a>b and a>c):
        return f"{n} is greater"
    elif(b>a and b>c):
        return f"{m} is greater"
    else:
        return f"{o} is greater"


n = int(input("enter no.1:"))
m = int(input("enter no.2:"))
o = int(input("enter no.3:"))

z = print(function(n,m,o)) 