i = 1
while i <= 100:
    if i % 3 == 0 and i % 15 != 0:
        print(f"{i} Fizz")
        i += 1
        continue
    elif i % 5 == 0 and i % 15 != 0:
        print(f"{i} Buzz")
        i += 1
        continue
    elif i % 15 == 0:
        print(f"{i} FizzBuzz")
        i += 1
        continue
    else:
        print(i)
        i += 1
        continue