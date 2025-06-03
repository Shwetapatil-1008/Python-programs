number = input("Enter a 4-digit number: ")

if len(number) != 4 :
    print("Please enter a valid 4-digit number.")

else:
    number = int(number)
    d1 = number // 1000
    print("First digit :",d1)
    d2 = number % 10
    print("Last digit :",d2)
    sum_of_digits = d1 + d2

    print(f"The sum of the first and last digits of {number} is: {sum_of_digits}")
