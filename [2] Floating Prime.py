import sympy

def main():
    listOfNum = []
     # count of each number of decimal for input number
    listOfDecimal =[]

    while(True):
        num = input()
        if num=="0.0":
            break
        else: 
            # count float decimal
            lenOfFloat = num[::-1].find('.')
            listOfDecimal.append(lenOfFloat)
            listOfNum.append(float(num))

    for index in range(len(listOfNum)):
        if isFloatingPrime(listOfNum[index], listOfDecimal[index]):
            print("TRUE")
        else:
            print("FALSE")


def isFloatingPrime(num, lenOfFloat):
    chanegFloatDigit = 10
    for _ in range(lenOfFloat):
        print
        if sympy.isprime(int(num*chanegFloatDigit)):
            return True
        chanegFloatDigit*=10
    return False


main()
