#Rock wins against Scissors
#Scissors wins against Paper
#Paper wins against Rock 
import random
user1_choice=(int(input("Enter your choice: 0 for Rock,1 for paper,2 for scissors . ")))
if user1_choice >= 3 or user1_choice <0:
    print("You entered invalid no,You lose.")
else:
    user2_choice=random.randint(0,2)
    print("user2_chose:")
    print (user2_choice)
    if (user2_choice == user1_choice):
      print("It's a draw.")
    elif user2_choice==0 and user1_choice== 2:
      print("You lose. ")
    elif user1_choice==0 and  user2_choice==2:
      print("You Win. ")
    elif user2_choice > user1_choice:
      print("You lose. ")
    elif user1_choice > user2_choice:
      print("You Win. ")

    