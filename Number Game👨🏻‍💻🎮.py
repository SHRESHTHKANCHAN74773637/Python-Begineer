''' Number Guessingⁿᵒ ᵐᵒᵈᵘˡᵉ '''
import time as tm
tm.sleep(1)
print("\n🅃🄷🄸🅂 🄸🅂 🄼🄰🄳🄴 🄱🅈 🅃🄴🄲🄷🄽🄸🄲🄰🄻\n🅁🄴🄱🄴🄻.\n")
tm.sleep(1)
print("We have randomly choosen a number between 1 to 20")
tm.sleep(1)
print("\nNow you have to guess the number which we have chosen for you and enter that number.\n")
tm.sleep(1)
loss = 0
i = 9
num = 7
tm.sleep(1)
print("\t🔥🔥𝙃𝙀𝙍𝙀 𝙔𝙊𝙐 𝙂𝙊💥💥\n")
while(i>loss):
    answer = int(input("=>Think of a number between 1 to 20: "))
    if answer==num:
        print("\n=>Congratulations you've won")
        break
    elif answer>20:
        loss + 1
        i = i - 1
        print("No. of Times you played: ",loss)
        print("Number of guesses you have: ",i)
        print("\n1 point have been added to number of guesses.")
        print("It is invalid")
        continue
    elif answer!=any:
        loss + 1
        i = i - 1
        print("No. of Times you played: ",loss)
        print("Number of guesses you have: ",i)
        print("\nYou took 1 number of guesses now.")
        print("\n=>Try again by adding ",num-answer)
        continue
    elif loss==9 and i==0:
        break
    else:
        break
