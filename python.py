import random

secret_number = random.randint(1,20)
chances = 5

print("Guess the number between 1 and 20. You have", chances, "chances.")

while chances > 0:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number correctly.")
        break
    else:
        chances -= 1
        if chances > 0:
            print("❌ Incorrect guess. You have", chances, "chances left.")
        else:
            print("😞 You're out of chances. The correct number was", secret_number)
            if chances==0:
               
                
                pay_again=input('you want to play again?(y/n)').lower()
                if pay_again!='y':                    
                   
                 print('thank you for playing')
