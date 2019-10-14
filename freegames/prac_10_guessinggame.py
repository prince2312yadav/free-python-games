import random
n=random.randint(0,9)
guess_count=0


while guess_count<3:
    b=int(input("Guess : "))
    guess_count+=1
    if b==n:
        print("You Win!!!!")

        break

else:
    print("\nYOU LOSE : LOSER")
    print(f"\nThe correct number was : {n}", )

input("\npress enter to exit")