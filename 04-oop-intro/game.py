import datetime
from random import randrange
from enum import Enum
import files
import jsonfile as jsonfile


class Sex(Enum):
    male = "man"
    female = "woman"


class Person:
    def __init__(self, nickname: str, sex: Sex):
        self.nickname = nickname
        self.sex = sex
        self.__birth = datetime.datetime.now()

    def __str__(self):
        return f"Nickname: {self.nickname}, sex: {self.sex}"

    def get_seconds_from_birth(self):
        actual_time = datetime.datetime.now()
        return int((actual_time - self.__birth).total_seconds())

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if sex in Sex:
            self.__sex = sex
        else:
            raise ValueError("Sex Value is not valid")

class Player(Person):
    def __init__(self, nickname: str, sex: Sex, state: str):
        super().__init__(nickname, sex)
        self.state = state
        self.count_of_games = 0
        self.wins = 0
        self.score = {"plus": 0, "minus": 0}

    def __str__(self):
        return f"Metoda predka: {super().__str__()}, state: {self.state}"

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        if value < 0:
            raise ValueError("Property wins hasn't negative value")
        else:
            self.__wins = value

    def win_rate(self):
        try:
            rate = (self.wins / self.count_of_games)* 100
        except Exception as error:
            return error
        else:
            return float("{:.2f}".format(rate))


class Match:
    def __init__(self, house_player: Player, guest_player: Player):
        self.h_player = house_player
        self.g_player = guest_player
        self.__datetime = datetime.datetime.now()
        self.hp_points = 0
        self.gp_points = 0
        self.__history = []

    def __str__(self):
        return f"{self.h_player.nickname} vs. {self.g_player.nickname} {self.hp_points}:{self.gp_points}"

    def __roll(self):
        while True:
            hp = randrange(1, 6)
            gp = randrange(1,6)
            if hp!=gp:
                break
        return 0 if hp > gp else 1

    def play(self):
        while self.hp_points < 10 and self.gp_points < 10:
            if self.__roll() == 0:
                self.hp_points += 1
            else:
                self.gp_points += 1
            self.__history.append(self.score())
        self.h_player.score["plus"] += self.hp_points
        self.h_player.score["minus"] += self.gp_points

        self.g_player.score["plus"] += self.gp_points
        self.g_player.score["minus"] += self.hp_points

        if self.hp_points > self.gp_points:
            self.h_player.wins += 1
        else:
            self.g_player.wins += 1

    def score(self):
        return self.hp_points, self.gp_points

    def get_history(self):
        return self.__history
# test


player1 = Player("Karel", Sex("man"), "CZE")
player2 = Player("Jana", Sex("woman"), "CZE")

# player.count_of_games = 555
# player.wins = 308
input("Pockej chvili a zadej enter")
# print(person, person.get_seconds_from_birth())
# print(player, player.get_seconds_from_birth())
# print(f"{player.win_rate()}%")
match = Match(player1, player2)
match.play()
print(str(match), f"\nHistorie: {match.get_history()}")

def load_players(json_file):
    players = []
    try:
        data = jsonfile.read(json_file)
    except Exception as error:
        return f"Error: {error}"
    else:
        for row in data:
            players.append(Player(row["nickname"], Sex(row["sex"], state(row["state"]))))
        return players

print(load_players("./players.json"))