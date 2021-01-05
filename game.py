import random


class game():
    def __init__(self,x):
        self.x=x
        wynik=random.randint(3, 8)
        if x == wynik:
            print('wygrales')
        else:
            print('try one more time')
        print('Wynik:', wynik)
        print('Twoja liczba: ',x)


game(3)