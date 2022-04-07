import random
from colorama import Fore , Back , Style

#My numbers
yplist = [random.randrange(1, 20) for i in range(5)]
lucky_num = [random.randrange(1, 10) for r in range(1)]
yplist.sort()
print("your lucky numbers", Fore.LIGHTMAGENTA_EX+str(yplist)+Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX+str(lucky_num) + Style.RESET_ALL)

# White balls
wblist = [random.randrange(1, 20) for i in range(5)]
pb1 = [random.randrange(1, 10) for r in range(1)]
wblist.sort()
print(" Today’s Powerball winning numbers. ", Fore.LIGHTMAGENTA_EX+str(yplist)+Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+str(pb1)+Style.RESET_ALL)
wblist.sort()
if yplist == wblist and lucky_num == pb1:
  print("You won the jackpot !! - 324,000,000$")


