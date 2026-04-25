import random

def welcome():
    print("welcom to this funny Game!")
    print("I will guess a number between 1 20 and,")
    print("and you have to guess it...")
    print("go go go!\n")
    

def finish(computer_num, count, record):
    print("\ngood game!")
    print(f"my number was {computer_num} and you found it in {count}")
    
    if record ==0 or record > count:
        print("new record")
        record = count
    else:
        print(f"best record so far: {record}\n")
        
    ans = input("do you want play again? (y/n) ")
    if ans.upper() in ['Y', 'YES', 'ARE']:
        return True, record
    else:
        return False

    
def win(computer_num, guess):
    return computer_num == guess


def answer(computer_num, guess):
    if computer_num < guess:
        return "ohhh. you went so large...mine is smaller!!"
    if computer_num > guess:
        return "my number is larger!!"
    return "wow! you won! good Guess!"


def get_a_guess():
    while True:
        ans = input("guess a number?  ")
        if ans.isdigit():
            return int(ans)
        else:
            print("pleas inter valid number!")

    
    
welcome()


continue_playing = True
record =0


while continue_playing:
    computer_num = random.randint(1, 20)
    guess = None
    count = 0
    
    while not win(computer_num, guess):
        guess = get_a_guess()
        count += 1
        print(answer(computer_num, guess))
        
    continue_playing, record = finish(computer_num, count,record)
        
    
