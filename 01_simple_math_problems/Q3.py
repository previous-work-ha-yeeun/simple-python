base = int(input("Enter the new base (between 2 and 9): "))
maximum = base ** 4 - 1
print(f"The maximum base 10 number you can enter is: {maximum}")
decimal_number = int(input("Enter the base 10 number: "))

remainder_d = decimal_number % base
quotient = decimal_number // base
print(quotient, remainder_d)

remainder_c = quotient % base
quotient = quotient // base
print(quotient, remainder_c)

remainder_b = quotient % base
quotient = quotient // base
print(quotient, remainder_b)

remainder_a = quotient % base
quotient = quotient // base
print(quotient, remainder_a)

print(f"The result of the base conversion is: {remainder_a}{remainder_b}{remainder_c}{remainder_d}")






