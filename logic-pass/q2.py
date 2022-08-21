def findPrimeNumbers(firstNumber, secondNumber):
    primes = []

    for i in range(firstNumber, secondNumber + 1):

        if (i == 1):
            continue
        
        flag = 1

        for j in range(2, i):
            if i % j == 0:
              flag = 0
              break

        if (flag == 1):
            primes.append(i)
    
    return primes

def app():
    firstNumber = input("\nEnter first number : ")
    secondNumber = input("\nEnter second number: ")

    if(firstNumber.isnumeric() and secondNumber.isnumeric()):
      print("Prime numbers between ", firstNumber, " and ", secondNumber, " are: ")
      print(findPrimeNumbers(int(firstNumber), int(secondNumber)))
    else: 
      print("Input error you should numbers expected !!")
      
app()