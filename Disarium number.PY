def is_disarium(num):
    digits = str(num)
    total = 0

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)

    if total == num:
        return True
    else:
        return False

num = int(input("Enter a number"))

if num > 0:
    if is_disarium(num):
        print(num, "is a Disarium Number")
    else:
        print(num, "is not a Disarium Number") 
else:
    print("Please enter a positive number")