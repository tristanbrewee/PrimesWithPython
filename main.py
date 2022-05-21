#User inputs max limit (only numbers)
while True:
    try:
        max = int(input("Till how many? "))
        break
    except:
        print("number please")

#Inistantiate list with True
numbers = []
for i in range(max):
    numbers.append(True)

inBetween = 0
i = 1
while i < len(numbers):
    #Print counter to know the program hasn't crashed (only useful for big upper limits)
    if i > inBetween:
        print("counter: ", inBetween)
        inBetween += 1000

    #Cross off all multiples of the current prime
    j = 2
    while True:
        try:
            crossOf = (i + 1) * j
            numbers[crossOf - 1] = False
            j += 1
        except:
            break

    #Go to the next prime
    try:
        i = numbers.index(True, (i+1))
    except:
        break

counter = 0
for x in range(len(numbers)):
    #Print all primes (10 per line)
    if numbers[x] == True:
        print(str(x + 1).ljust(15), end = "")
        counter += 1
    if counter == 10:
        print()
        counter = 0