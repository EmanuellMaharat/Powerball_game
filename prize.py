from game import *

def matchnumbers():
 prize = [p for p in yplist if p in wblist]
 if len(prize) == 5 :
  print("Congrats You guessed right 5 white balls , you won 1,000,000$ !")
 if len(prize) == 4 :
  print("Greetings You guessed right 4 white balls, you won 100$ !")
 if len(prize) == 4 and lucky_num == pb1 :
  print("Greetings You guessed right 4 white balls and powerball , you won 10,000$ !")
 print(prize)
 if len(prize) == 3 :
  print("Congrats You guessed right 3 white balls ,  you won 7$ !")
 if len(prize) == 3 and lucky_num == pb1 :
  print("Congrats You guessed right 3 white balls and powerball , you won 100$ !")
 if len(prize) == 2 :
  print("Congrats You guessed right 2 white balls , you won 7$ !")
 if len(prize) == 1 and lucky_num == pb1 :
  print("Congrats You guessed right 1 white ball and lucky number , you won 4$ !")
 if lucky_num == pb1:
   print("You guessed right powerball , you won 4$ !")
 if len(prize) <= 1 and lucky_num != pb1:
   print("Try again")
#matchnumbers()

