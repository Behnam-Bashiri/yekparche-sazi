
numbers = []

def shower():
    for i in numbers:
        print(i)

def gamer(inpU,inpS):
    if inpU != 'HOP':
        if inpU%5 == 0 and inpS%5 == 0:
            numbers.append("HOP")
        else:
            numbers.append(inpU)
            numbers.append(inpS)
    else:
        numbers.append("HOP")
        numbers.append(inpS)
    print(numbers)

def input_userdata():
    user_input = input("enter number hop :\->")
    last_number = numbers[-1]
    if user_input != "HOP":
        if int(user_input)%5==0:
            print('game over ! HOP !!!')
            exit()
        user_input = int(user_input)
        if last_number!="HOP" and user_input == last_number+1:
            if user_input%5 ==4 :
                numbers.append(user_input)
                numbers.append("HOP")
                print(numbers)
                input_userdata()
            elif last_number%5 ==4 and not(user_input.startswith("HOP")):
                print("Game Over !")
            else:
                sys_input = user_input+1
                gamer(user_input,sys_input)

        elif last_number!="HOP" and user_input != last_number+1:
            print("wrong order !")
            print(numbers)
        elif last_number=="HOP":
            numbers.append(numbers[-2]+2)
            print(numbers)
            input_userdata()
    elif user_input == "HOP":
        if last_number%5 == 4:
            sys_input = last_number+2
            gamer('HOP',sys_input)



print("HI this is HOP game :) \n")
first_input = int(input("enter number hop :\->"))
if first_input == 1:
    sys_input = first_input+1
    gamer(first_input,sys_input)
else:
    print("wrong number !")
    exit()

while True:
    input_userdata()

