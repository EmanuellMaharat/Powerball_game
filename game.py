import random

#My numbers
yplist = [random.randrange(1, 20) for i in range(5)]
lucky_num = [random.randrange(1, 10) for r in range(1)]
yplist.sort()
print("your lucky numbers", yplist)
print(lucky_num)

# White balls
wblist = [random.randrange(1, 20) for i in range(5)]
pb1 = [random.randrange(1, 10) for r in range(1)]
wblist.sort()
print(" Today’s Powerball winning numbers. ", yplist)
print(pb1)
wblist.sort()
if yplist == wblist and lucky_num == pb1:
  print("You won the jackpot !! - 324,000,000$")


