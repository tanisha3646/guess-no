n=18
i=10
t='Y'
while(t.upper()=='Y'):
    print("\tHello! Welcome to the guessing game")
    while(True):
        if i>0:
            print("\tTotal remaining guesses are: ",i)
            inp=int(input("Enter your guess between 0-100 :\n"))
            if inp>n:
                print("Oops...Try again\nThe number is smaller than your guess!")
                i=i-1
                continue
            elif inp<n:
                print("Oops...Try again\nThe number is still larger than your guess!")
                i=i-1
                continue
            else:
                print("\t\tCongratulations! You won")
                break
        print("\t\tOops! Game over\n\t\tBetter luck next time")
        break
    t=input("\tDo you want to continue(Y/N)\n")