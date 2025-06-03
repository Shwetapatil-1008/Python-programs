# For n digit numbers
no=int(input("Enter 3 digit number : "))
no_str=str(no)
reverse_str=no_str[::-1]

reverse_int=int(reverse_str)

print(f"The reverse order of {no} is = ",reverse_int)
