import numpy as np
import random


class Board():
    def __init__(self):
        pass

    def is_occupated(self):
        pass

class Player:
    number_of_players = 0
    tiles_arr = np.arange(40)
    money_ammount = 1500
    tile = 0

    def __init__(self, name, ):
        self.name = name
        Player.number_of_players += 1

    def make_move(self):
        move = Player.roll(self)
        if not move:
            Player.go_to_jail(self)
            print("Your roll pair 3 times, you are going to jail!")
        else:
            self.tile += Player.tiles_arr[Player.tile] + move
            if self.tile > 39:
                self.tile = self.tile - 40
            print("Your roll = ", move, "You are going to: ", move+self.tile, " tile.")

    def roll(self):

        for i in range(3):
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            if a != b:
                return a + b
        return False

    def pay_rent(self):
        pass

    def go_to_jail(self):
        pass

    def buy_estate(self):
        pass

    def




print("Witamy w monopoly dla biedaków!")
Player1 = Player(input("Podaj imie pierwszego gracza:"))
Player2 = Player(input("Podaj imie drugiego gracza:"))
d = input("Dodać kolejnego gracza? Y/N")
if d == "Y":
    Player3 = Player(input("Podaj imie trzeciego gracza: "))
    d = input("Dodać kolejnego gracza? Y/N")
    if d == "Y":
        Player4 = Player(input("Podaj imie trzeciego gracza: "))


while True:
    turn = 1
    P = 'Player' + f"{turn}"
    tile = P.tile
    nieruchomosci = [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39, 5, 15, 25, 35, 12, 28]
    chance = [7,22,36]
    chest = [2, 17,33]


    if tile in nieruchomosci:
        if is_occupated(tile):   # 2.2. Jeśli wolne:
            ptint("czy chcesz kupić tą nieruchomość?")
            if input("Y/N"):
                P.buy_estate()   # 2.2.1 Kup
            else:
                P.licitation()    # 2.2.2 Oddaj na licytacje innym
        else:
            P.pay_rent()          # 2.1. Jeśli zajęte zapłać czynsz

    elif tile in chance:
        P.chance()

    elif tile in chest:
        P.open_community_chest()

    elif tile == 30:
        P.go_to_jail()

    elif tile == 4:
        P.pay_rent(200)

    elif tile == 38:
        P.pay_rent(100)

    elif tile == 10 or 20:
        P.wait()
            
                    
