import random

print()
#My numbers
yplist = [random.randrange(1, 20) for i in range(5)]
lucky_num = [random.randrange(1, 10) for r in range(1)]
yplist.sort()
print("your lucky numbers",yplist)
print(lucky_num)

#White balls
wblist = [random.randrange(1, 20) for i in range(5)]
pb1 = [random.randrange(1, 10) for r in range(1)]
wblist.sort()
print(" Today’s Powerball winning numbers. ",yplist)
print(pb1)
wblist.sort()

if yplist == wblist and lucky_num == pb1 :
 print("You won the jackpot !! - 324,000,000$")
def matchnumbers():
 prize = [p for p in yplist if p in wblist]
 if len(prize) == 5 :
  print("Congrat, you won 1,000,000$ !")
 if len(prize) == 4 :
  print("Congrat, you won 100$ !")
 if len(prize) == 4 and lucky_num == pb1 :
  print("Congrat, you won 10,000$ !")
 print(prize)
 if len(prize) == 3 :
  print("Congrat, you won 7$ !")
 if len(prize) == 3 and lucky_num == pb1 :
  print("Congrat, you won 100$ !")
 if len(prize) == 2 :
  print("Congrat, you won 7$ !")
 if len(prize) == 1 and lucky_num == pb1 :
  print("Congrat, you won 4$ !")
 if lucky_num == pb1:
   print("powerball is correct , you won 4$ !")
 if len(prize) <= 1 and lucky_num != pb1:
   print("Try again")
matchnumbers()


