import random 

def user_input():
    for i in range(10):
        print("1. for 🪨.\n2. for 📃.\n3. for ✂️.\n4. for exit")
        choice=int(input("enter the sign (using number between 1 to 3):"))
        input_checker(choice)
    
    
def input_checker(choice):
    comp_choice=random.randint(1,3)
    result=0
    if choice==1 and comp_choice==2:
        print("you selected 🪨 and computer selected 📃.")
        print("you lose.")
        result=result
    elif choice ==1 and comp_choice==1:
        print("you selected 🪨 and computer selected 🪨.")
        print(" Draw")
        result = result

    elif choice==1 and comp_choice==3:
        print("you selected 🪨 and computer selected ✂️.")
        print("you won")
        result+=1

    elif choice==2 and comp_choice==1:
        print("you selected 📃 and computer selected 🪨.")
        print("you won")
        result+=1

    elif choice==2 and comp_choice==3:
        print("you selected 📃 and computer selected ✂️.")
        print("you lose")
        result=result

    elif choice == 2 and comp_choice == 2:
        print("you selected 📃 and computer selected 📃")
        print(" Draw")
        result = result

    elif choice==3 and comp_choice==1:
        print("you selected ✂️ and computer selected 🪨.")
        print("you won")
        result+=1

    elif choice==3 and comp_choice==2:
        print("you selected ✂️ and computer selected 📃.")
        print("you won")
        result+=1
    
    elif choice ==3 and comp_choice==3:
        print("you selected ✂️ and computer selected ✂️")
        print(" Draw")
        result = result

    elif choice==4:
        exit()
    else:
        print("game over ")

    print("your score is:", result )


user_input()

