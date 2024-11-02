import random  # Import
def displayMenu():
    print("DIFFICULTY LEVEL")  #menu
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
def randomInt(level):
    if level == 1:  #easy
        return random.randint(1, 9)
    elif level == 2:  #moderate
        return random.randint(10, 99)
    elif level == 3:  #advanced
        return random.randint(1000, 9999)
def decideOperation():
    return random.choice(['+', '-'])  #operation
def displayProblem(level):
    num1 = randomInt(level)  #number1
    num2 = randomInt(level)  #number2
    operation = decideOperation()  #op
    if operation == '-' and num1 < num2:  #no-neg
        num1, num2 = num2, num1
    correct_answer = num1 + num2 if operation == '+' else num1 - num2  #answer
    print(f"{num1} {operation} {num2} = ?")  # Print
    return correct_answer  #return
def quiz():
    score = 0  #init-score
    displayMenu()  #showing menu
    level = int(input("Choose difficulty level (1, 2, or 3): "))  # Input
    for i in range(10):  # Loop
        print(f"\nQuestion {i + 1}:")  #question
        correct_answer = displayProblem(level)  #problem
        user_answer = int(input("Your answer: ")) #answer
        if user_answer == correct_answer:  #correctt
            print("Correct!")
            score += 10  #Add-10
        else:
            print("Incorrect. Try again.")  #retry
            user_answer = int(input("Second attempt: "))  #attempt2
            if user_answer == correct_answer:  # correct
                print("Correct!")
                score += 5  #add5
            else:
                print("Incorrect again.")  #incorrect
    print(f"\nYour final score is: {score} / 100")  #final-score
    if score >= 90:
        print("Grade: A+")  #grade
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    elif score >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
quiz()  #eun the code