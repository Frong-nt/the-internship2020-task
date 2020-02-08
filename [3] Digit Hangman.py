def main():
    finalScore, num = 0, input().split(' ')
    # to keep list of numbers that wrong guessing
    falseNum = []
    for _ in range(len(num)):
        print('_', end=' ')
    # for print new line
    print()

    # set of number that  correct guessing
    correctGuessingNum = set()
    for _ in range(5):
        guessingNum, status,  = input(), False
        # to keep score for each number that guess correct
        score = 0
        for index in range(len(num)):
            if num[index] == guessingNum:
                print(num[index], end=' ')
                score +=1
                status = True
                correctGuessingNum.add(num[index])
            elif num[index] in correctGuessingNum:
                print(num[index], end=' ')
            else:
                print('_', end=' ')
        # in case of user guess incorrect then these number keep into falseNum
        if not status:
            falseNum.append(guessingNum)     
        
        
        finalScore += score    
        # in case of when user incorrect guessing number
        for index in range(len(falseNum)): 
            print(falseNum[index], end = ' ')
        # for print new line
        print()
    #it's time to print final score
    print(finalScore)
        

main()
