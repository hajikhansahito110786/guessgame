import random
print("Computer has selected one guess no try to findout")
guessno:int=random.randint(1,10)
#print(guessno)
try:
    while True:
        youranswer:int=int(input("your number plz"))

        if youranswer==guessno:
            print("corect you won ")
            break
        elif youranswer < guessno:
            print("little bit more")
        elif youranswer > guessno:
            print("littlebit less")
  
        
except ValueError:
    print("enter coorect entry")



