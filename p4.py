no=int(input("Enter 3 digit number : "))

d1=no%10
no=int(no/10)
d2=no%10
no=int(no/10)
d3=no%10

print(f"The reverse order of {no} is = ",d1*100+d2*10+d3*1)
