"""
age = 30
n = 0
while n < 3:
    guess_age = int(input("guess age: "))
    n += 1
    if guess_age == age:
        print("you are right!")
        break
    else:
        print("you are wrong,you have 3 chance")
"""

age = 30
yes = {"yes","y","YES","Y"}
no = {"no","n","NO","N"}
n = 0
while n < 3:
    guess_age = int(input("guess age: "))
    if guess_age == age:
        print("you are right!")
        break
    elif guess_age < age:
        print("try bigger,you have 3 chance")
    else:
        print("try smaller,you have 3 chance")
    n += 1
    while n == 3:
            choice = input("one more try?(y|n)")
            if choice == 'y' or choice == 'Y':
                n = 0
                continue
            elif choice == 'n' or choice == 'N':
                print("good bye!")
                break
            else:
                print("type regular please!")





