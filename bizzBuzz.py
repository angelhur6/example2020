

number = 100
i = 0

while i < number:
    i = i +1
    if i % 3 == 0 and i %5 != 0:
        print("Fizz")
        continue
    if i % 5 == 0 and i %3 != 0:
        print("Buzz")
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
    



