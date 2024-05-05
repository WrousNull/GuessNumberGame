#Guess number
import random
MAX = 20
ans = random.randint(0,MAX)
cnt = 1
ISPRIME = False
isPrime = False
FUCK = False
trys = []
extra = 0
vip = ['王佳鑫']
tips = [f"Please enter a number from 0 to {MAX}.",
        "Please try again:",
        "No,is too small.",
        "No,is too big.",
        "tellmeanswer"]
name = input("Hello player,what's your name?")
print(f"OK,dear {name},let's play a game called Guessing Number !")
while not isPrime:
    num = input(f"guess a number that from 0 to {MAX}:")
    if num == tips[4]:
        extra += 1
        ISPRIME = True
        if extra >= 5:
            print(f"Fucking {name},you have using it {extra} times,You fucking asshole.")
            print(f"The game will become more difficult.")
            print("If you escape the game,you will be a shit man.")
            MAX += 10
            ISPRIME = False
            FUCK = True
            continue
    if not ISPRIME and num not in str(list(range(0,MAX+1))):
        print(tips[0]+"\n")
        continue
    elif num == ' ' or num == '\n' or num == '':
        continue
    else:
        if ISPRIME:
            trys.append(cnt)
            print("Congratulations!\n")
            print(f"Well,you have tried {cnt} times to guess it.")
            choice = input("Do you want to play again?\nEnter y to play,enter the other to quit:")
            if choice == 'y':
                ans = random.randint(0, MAX)
                cnt = 1
                isPrime = False
                ISPRIME = False
                continue
            else:
                if not FUCK:
                    print(f"Your best grade is {min(trys)} times.\nHave a nice day,{name.title()}.")
                    input()
                    break
                else:
                    print(f"{name.upper()},you are a clown.")
                    input()
                    break
        isPrime = True
        num = int(num)
        if isPrime and num != ans:
            if num > ans:
                print(tips[3]+"\n")
                cnt += 1
                isPrime = False
                continue
            else:
                print(tips[2]+"\n")
                cnt += 1
                isPrime = False
                continue
        else:
            trys.append(cnt)
            print("Congratulations!\n")
            print(f"Well,you have tried {cnt} times to guess it.")
            choice = input("Do you want to play again?\nEnter y to play,enter the other to quit:")
            if choice == 'y':
                ans = random.randint(0, MAX)
                cnt = 0
                isPrime = False
                continue
            else:
                if not FUCK:
                    print(f"Your best grade is {min(trys)} times.\nHave a nice day,{name.title()}.")
                    input()
                    break
                else:
                    print(f"{name.title()},you are a clown.")
                    input()
                    break


