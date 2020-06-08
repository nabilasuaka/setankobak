C = "\033[94;m"
G = "\033[92;m"
r = "\033[0;m"
P = "\033[93;m"
def banner():
    print("""
    {0}____  __  ___ ___   ____
   / __/ /  |/  // _ ) / __/
  _\ \  / /|_/ // _  |/ _/
 /___/ /_/  /_//____//_/ v{2}1.1{0}2020.
 {1}[ {2}Semua Kekuatan Pasti Ada Kelemahan{1} ]{1} 
 {1} [ {2}Created by : Setan Kobak{1} ]{1}
            """.format(C,r,G))
def menu():
    print(f"{C}1{r} from friendlist")
    print(f"{C}2{r} from likes on post")
    print(f"{C}3{r} by search name")
    print(f"{C}4{r} from group (only takes 100 user)")
    print(f"{C}5{r} from friend friendlist")
    print(f"{C}6{r} from hashtag ")
    print(f"{C}7{r} Re-check result")
