def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif number % 2 == 1:
        result = (number * 3) + 1
        print(result)
        return result

print("Please enter a number: ")
userInput = input()
userNumber = int(userInput)
while userNumber != 1:
    userNumber = collatz(userNumber)