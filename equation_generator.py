import random
# python version is 3.13.1


def makes_equation():
    """makes an equation of the form a * x = b after setting values of a and x"""
    a = random.choice([i for i in range(-22, 23) if i != 0])  # giving value for 'a' except zero
    x = random.randint(-22, 22)  # giving a solution for x
    b = a * x
    return a, x, b


def asks_question(a, b):
    """asks user to solve for x in the equation"""
    try:
        users_answer = int(input(f"solve for x: {a} × x = {b}\nyour answer: ")) # get input and make into integer
        return users_answer
    except ValueError:
        print("invalid input. please enter an integer.")
        return asks_question(a, b)  # get input again if it isn't an integer


score = 0 # sets the users initial score

for _ in range(5):
    a, correct_x, b = makes_equation()
    users_answer = asks_question(a, b) # prompting user for an answer

    if users_answer == correct_x:
        print("correct\n")
        score += 1
    else:
        print(f"wrong, answer is {correct_x}\n") 

print(f"Final score {score}/{5}")
